import re

from translate import translate


def test_translate_examples_in_readme():
    # 1984年的四川省涪陵地区南川县
    # 对应于2018年的重庆市南川区
    assert translate("512323", 1984, 2018) == ["500119"]

    # 2000年的湖南省衡阳市城北区
    # 对应于2018年的湖南省衡阳市石鼓区、蒸湘区
    assert translate("430404", 2000, 2018) == ["430407", "430408"]

    # 2010年的北京市西城区
    # 对应于2000年的北京市西城区、宣武区
    assert translate("110102", 2010, 2000) == ['110102', '110104']

def test_translate_code_change():
    '''
    1989年，锦西市升为地级市，锦州市的葫芦岛区……划归锦西市管辖
    1994年，锦西市更名为葫芦岛市，葫芦岛区更名为龙港区
    '''
    '''
     * 辽宁省-锦州市-葫芦岛区(210705)
    -> 辽宁省-锦西市-葫芦岛区(211405) 1989
    -> 辽宁省-葫芦岛市-龙港区(211403) 1994
    '''
    assert translate("210705", 1984, 1988) == ['210705']
    assert translate("210705", 1984, 1989) == ['211405']
    assert translate("210705", 1984, 1990) == ['211405']
    assert translate("210705", 1984, 1993) == ['211405']
    assert translate("210705", 1984, 1994) == ['211403']
    assert translate("210705", 1984, 1995) == ['211403']
    assert translate("210705", 1984, 2018) == ['211403']
    assert translate("211405", 1989, 1993) == ['211405']
    assert translate("211405", 1989, 1994) == ['211403']
    assert translate("211405", 1989, 1995) == ['211403']
    assert translate("211405", 1989, 2018) == ['211403']

    # 反向查询
    assert translate("211405", 1989, 1984) == ['210705']
    assert translate("211403", 1994, 1984) == ['210705']
    assert translate("211403", 1995, 1989) == ['210705']
    assert translate("211403", 1995, 1990) == ['211405']
    assert translate("211403", 2018, 1984) == ['210705']


def test_translate_merge():
    '''
    2010年：撤销北京市西城区、宣武区，设立新的北京市西城区，
    以原西城区、宣武区的行政区域为西城区的行政区域
    '''
    '''
     * 北京市-宣武区(110104)
    -> 北京市-西城区(110102) 2010
    '''
    assert translate("110104", 2000, 2010) == ['110102']
    # 反向查询
    assert translate("110102", 2010, 2000) == ['110102', '110104']


def test_translate_split():
    '''
    1997年：
    （1）撤销曲靖地区和县级曲靖市，设立地级曲靖市。
    （2）曲靖市设立麒麟区和沾益县。
    麒麟区辖原县级曲靖市的……4个镇和6个乡。
    沾益县辖原县级曲靖市的……2个镇和8个乡。
    '''
    '''
     * 云南省-曲靖地区-曲靖市(532201)
    -> 云南省-曲靖市-麒麟区(530302), 云南省-曲靖市-沾益县(530328) 1997
    '''
    assert translate("532201", 1990, 1997) == ['530302', '530328']
    # 反向查询
    assert translate("530302", 1997, 1996) == ['532201']
    assert translate("530328", 1997, 1996) == ['532201']


def test_translate_full():
    """
    全量数据测试
    """
    current_code_list: list[str] = []
    with open("tables/2022.csv", encoding="utf-8") as f:
        for line in f:
            cells = line.strip().split(",")
            if len(cells) < 2:
                continue
            if re.match(r"^\d{6}$", cells[0]) is not None:
                current_code_list.append(cells[0])
    for year in range(1984, 2023):
        with open(f"tables/{year}.csv", encoding="utf-8") as f:
            for line in f:
                cells = line.strip().split(",")
                if len(cells) < 2:
                    continue
                if re.match(r"^\d{6}$", cells[0]) is not None:
                    code = cells[0]
                    name = cells[1]
                    changed_code_list: list[str] = translate(code, original_year=year)
                    for changed_code in changed_code_list:
                        # assert changed_code in current_code_list
                        if changed_code not in current_code_list:
                            print(
                                f"year: {year}, code: {code}, name: {name} -> {changed_code} not in current code list"
                            )
