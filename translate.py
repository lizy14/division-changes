# coding: utf-8
import os
import sys
if sys.version_info[0] == 2:
    print("Python 2 is not supported")
    sys.exit()
try:
    from ruleloader import load_code_changes, load_name_changes, load_merges, load_splits
except:
    from .ruleloader import load_code_changes, load_name_changes, load_merges, load_splits


def code_to_readable(code, year):
    a, b, c = "", "", ""
    with open(path_wrapper('tables/{}.csv'.format(year)), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith(code):
                a = line.split(',')[1]
            if not code.endswith("00") and line.startswith(code[0:4] + "00"):
                b = line.split(',')[1]
            if not code.endswith("0000") and line.startswith(code[0:2] + "0000"):
                c = line.split(',')[1]
    result = ""
    for t in [c, b, a]:
        if t:
            result += t + "-"
    level = '县级'
    if code.endswith('00'):
        level = '地级'
    if code.endswith('0000'):
        level = '省级'
    return result[:-1] + '[{}]({})'.format(level, code)

MIN_SUPPORTED_YEAR = 1984
MAX_SUPPORTED_YEAR = 2018

def translate(code, original_year, target_year=MAX_SUPPORTED_YEAR, verbose=False):
    if original_year < MIN_SUPPORTED_YEAR or original_year > MAX_SUPPORTED_YEAR:
        raise ValueError(f"仅支持{MIN_SUPPORTED_YEAR}年至{MAX_SUPPORTED_YEAR}年的行政区划代码转换，您指定的起始年份{original_year}超出范围")
    if target_year < MIN_SUPPORTED_YEAR or target_year > MAX_SUPPORTED_YEAR:
        raise ValueError(f"仅支持{MIN_SUPPORTED_YEAR}年至{MAX_SUPPORTED_YEAR}年的行政区划代码转换，您指定的目标年份{target_year}超出范围")
    codes = [str(code)]
    if original_year < target_year:
        for year in range(original_year - 1, target_year + 1):
            old_codes = codes
            codes = []
            for old_code in old_codes:
                if year in merges and old_code in merges[year]:
                    codes.append(merges[year][old_code])
                elif year in splits and old_code in splits[year]:
                    codes += splits[year][old_code]
                elif year in code_changes and old_code in code_changes[year]:
                    codes.append(code_changes[year][old_code])
                elif year in name_changes and old_code in name_changes[year]:
                    codes.append(name_changes[year][old_code])
                else:
                    codes.append(old_code)
            if verbose and old_codes != codes:
                print('->', ', '.join([code_to_readable(code, year) for code in codes]), year)
    elif original_year > target_year:
        for year in range(original_year, target_year - 1, -1):
            old_codes = codes
            codes = []
            for old_code in old_codes:
                if year in demerges and old_code in demerges[year]:
                    codes.append(old_code)
                    codes += demerges[year][old_code]
                elif year in unsplit and old_code in unsplit[year]:
                    codes.append(unsplit[year][old_code])
                elif year in reverse_code_changes and old_code in reverse_code_changes[year]:
                    codes.append(reverse_code_changes[year][old_code])
                elif year in reverse_name_changes and old_code in reverse_name_changes[year]:
                    codes.append(reverse_name_changes[year][old_code])
                else:
                    codes.append(old_code)
            if verbose and old_codes != codes:
                print('<-', ', '.join([code_to_readable(code, year) for code in codes]), year)
    else:
        if verbose:
            print("您指定的起始年和目标年相同，无需转换")
    return codes

def get_code(name, year):
    results = []
    with open(path_wrapper('tables/{}.csv'.format(year)), encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(',')
            if(len(cells) < 2):
                continue
            if cells[1].startswith(name):
                results.append(cells[0])
    return results



def execute_query(code, year):
    print(' *', code_to_readable(code, year))
    translate(code, int(year), verbose=True)
    print()

def main():
    DEFAULT_YEAR = MIN_SUPPORTED_YEAR
    # REPL
    try:
        import readline
    except:
        pass

    while True:
        try:
            query = input('>> ').split(' ')
        except EOFError:
            print('Bye!')
            break
        code_raw = query[0]
        if(len(query) > 1):
            year = query[1]
        else:
            year = DEFAULT_YEAR
        if not code_raw.isnumeric():
            codes = {}
            while True:
                year_codes = get_code(code_raw, int(year))
                for year_code in year_codes:
                    if year_code not in codes:
                        codes[year_code] = year

                year += 1
                if year > MAX_SUPPORTED_YEAR:
                    break
            for code in codes:
                execute_query(code, codes[code])
            if len(codes) == 0:
                print("没有找到名称以“{}”开头的县级及以上行政区".format(code_raw))
                continue
        else:
            code = code_raw
            execute_query(code, year)


def path_wrapper(filename):
    return os.path.join(os.path.dirname(__file__), filename)


merges = load_merges(path_wrapper('rules-handwritten/code-merges.csv'))
splits = load_splits(path_wrapper('rules-handwritten/code-splits.csv'))
code_changes = load_code_changes(path_wrapper('rules-generated/code-changes.csv'))
name_changes = load_name_changes(path_wrapper('rules-generated/name-changes.csv'))

# 反向查询所需数据结构
demerges = {}
for year, merge in merges.items():
    for old, new in merge.items():
        if new in demerges.get(year, {}):
            demerges[year][new].append(old)
        else:
            demerges.setdefault(year, {})[new] = [old]

unsplit = {}
for year, split in splits.items():
    for old, news in split.items():
        for new in news:
            unsplit.setdefault(year, {})[new] = old

reverse_code_changes = {}
for year, changes in code_changes.items():
    for old, new in changes.items():
        reverse_code_changes.setdefault(year, {})[new] = old

reverse_name_changes = {}
for year, changes in name_changes.items():
    for old, new in changes.items():
        reverse_name_changes.setdefault(year, {})[new] = old


if __name__ == "__main__":
    main()
