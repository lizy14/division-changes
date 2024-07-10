def load_code_changes(filename):
    code_changes = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(",")
            change_year = int(cells[0].split("-")[1])
            old = cells[1]
            new = cells[2]
            if change_year not in code_changes:
                code_changes[change_year] = {}
            code_changes[change_year][old] = new
    return code_changes


def load_name_changes(filename):
    name_changes = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(",")
            change_year = int(cells[0].split("-")[1])
            code = cells[1]
            if change_year not in name_changes:
                name_changes[change_year] = {}
            name_changes[change_year][code] = code
    return name_changes


def load_merges(filename):
    merges = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            [change_year, old, new] = line.strip().split(",")
            change_year = int(change_year)
            if change_year not in merges:
                merges[change_year] = {}
            merges[change_year][old] = new
    return merges


def load_splits(filename):
    splits = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(",")
            change_year = int(cells[0])
            old = cells[1]
            if change_year not in splits:
                splits[change_year] = {}
            splits[change_year][old] = cells[2:]
    return splits

def load_dumps(filename):
    dumps = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(",")
            change_year = int(cells[0])
            new = cells[3]
            if change_year not in dumps:
                dumps[change_year] = {}
            dumps[change_year][new] = cells[1:]
    return dumps

