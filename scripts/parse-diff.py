import re
import os
import sys
from ruleloader import load_merges, load_splits

def load_diff(diff_filename):
    addition_lines = []
    deletion_lines = []

    with open(diff_filename) as f:
        for line in f:
            if line.startswith('<'):
                deletion_lines.append(line.strip())
            elif line.startswith('>'):
                addition_lines.append(line.strip())
    return addition_lines, deletion_lines


def extract_name(fullname):
    name = fullname
    name = re.sub(r'(市|县|区|地区)$', '', name)
    name = re.sub(r'((汉|阿昌|白|保安|布朗|布依|朝鲜|达斡尔|傣|德昂|侗|东乡|独龙|鄂伦春|俄罗斯|鄂温克|高山|仡佬|哈尼|哈萨克|赫哲|回|基诺|京|景颇|柯尔克孜|拉祜|黎|傈僳|珞巴|满|毛南|门巴|蒙古|苗|仫佬|纳西|怒|普米|羌|撒拉|畲|水|塔吉克|塔塔尔|土|土家|佤|维吾尔|乌兹别克|锡伯|瑶|彝|裕固|藏|壮)族)+自治', '', name)
    return name




def main(diff_filename):
    year = os.path.split(diff_filename)[1].split('.')[0]

    addition_lines, deletion_lines = load_diff(diff_filename)
    merges = load_merges('./rules-handwritten/code-merges.csv')
    splits = load_splits('./rules-handwritten/code-splits.csv')

    additions = {}
    for line in addition_lines:
        try:
            [code, fullname] = line[2:].split(',')
            # if code.endswith("00"):
                # print('skipping: ', [code, fullname], file=sys.stderr)
                # continue
            name = extract_name(fullname)
            if name in additions:
                print('duplicate additions: ', [code, fullname], additions[name], file=sys.stderr)
            else:
                additions[name] = [code, fullname]
                additions[code] = [code, fullname]
        except ValueError:
            pass


    # output files
    code_removals_unaccounted_for = open('./rules-generated/code-removals-unaccounted-for.log', 'a')
    code_changes = open('./rules-generated/code-changes.csv', 'a')
    name_changes = open('./rules-generated/name-changes.csv', 'a')

    for line in deletion_lines:
        try:
            [code, fullname] = line[2:].split(',')
        except ValueError:
            continue
        
        change_year = int(year.split('-')[1])
        if change_year in merges and code in merges[change_year]:
            continue
        if change_year in splits and code in splits[change_year]:
            continue
        

        name = extract_name(fullname)
        if name in additions:
            [[deleted_code, deleted_name], [added_code, added_name]] = [[code, fullname], additions[name]]
            if (((not (deleted_code.endswith("00"))) and (not (added_code.endswith("00")))) or ((deleted_code.endswith("00")) and (added_code.endswith("00")))):
                print(','.join([year, deleted_code, added_code, deleted_name]), end='', file=code_changes)
                if deleted_name != added_name:
                    print(' -> ' + added_name, file=code_changes)
                else:
                    print(file=code_changes)
                continue

        if code in additions:
            if (((not (code.endswith("00"))) and (not (additions[code][0].endswith("00")))) or ((code.endswith("00")) and (additions[code][0].endswith("00")))):
                print(','.join([year, code, fullname, additions[code][1]]), file=name_changes)
                continue

        print(year, code, fullname, file=code_removals_unaccounted_for)

if __name__ == '__main__':
    main(sys.argv[1])
