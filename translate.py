import os
try:
    from .ruleloader import load_code_changes, load_name_changes, load_merges, load_splits
except ImportError:
    from ruleloader import load_code_changes, load_name_changes, load_merges, load_splits
    
def code_to_readable(code, year):
    a, b, c = "", "", ""
    with open(path_wrapper('tables/{}.csv'.format(year))) as f:
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

def translate(code, original_year, verbose=False):
    codes = [str(code)]
    for year in range(original_year - 1, 2018): # safe margin
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
            print('->', [code_to_readable(code, year) for code in codes], '-', year)
    return codes

def get_code(name, year):
    with open(path_wrapper('tables/{}.csv'.format(year))) as f:
        for line in f:
            cells = line.strip().split(',')
            if(len(cells) < 2):
                continue
            if cells[1].startswith(name):
                return cells[0]

def execute_query(code, year):
    print(' *', code_to_readable(code, year))
    translate(code, int(year), verbose=True)

def main():
    DEFAULT_YEAR = 1984
    # REPL
    import readline
    while True:
        try:
            print()
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
            code = None
            while True:
                code = get_code(code_raw, int(year))
                if code is not None:
                    execute_query(code, year)
                    break
                year += 1
                if year > 2018:
                    break
            if code is None:
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

if __name__ == "__main__":
    main()
