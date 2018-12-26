# 行政区划代码及变更整理步骤


## 1. 爬取历年行政区划变更文字说明
* `./retrieve-descriptions`
* 得到 `./descriptions/source-b/1999.txt`

## 2. 爬取历年代码表 
* `./retrieve-tables.sh`
* `./parse-tables.py`
* 得到 `./tables/1999.csv`

## 3. 比对相邻年的代码表
* `./generate-diff.sh`
* 得到 `diffs/1999-2000.diff`

## 4. 根据比对结果生成规则
* `./parse-diff.sh`
* 得到 `./rules-generated/code-changes.csv`, `./rules-generated/name-changes.csv`
* 匹配失败列表：`./rules-generated/code-removals-unaccounted-for.log` 列出这样的代码，它们被删除了，但在当年新增代码中找不到对应的新代码

## 5. 人工核对
对照文字说明检查匹配失败列表，编写`./rules-handwritten/code-merges.csv`, `./rules-handwritten/code-splits.csv`

## 6. 大功告成
`./translate.py`
```
> 南川
 * 四川省-涪陵地区-南川县[县级](512323)
-> 四川省-涪陵地区-南川市[县级](512302) - 1994
-> 四川省-涪陵市-南川市[县级](517081) - 1995
-> 重庆市-南川市[县级](500384) - 1997
-> 重庆市-南川区[县级](500119) - 2006
```
```
> 广安
 * 四川省-南充地区-广安县[县级](512925)
-> 四川省-广安地区-广安县[县级](513622) - 1993
-> 四川省-广安市[地级](511600) - 1998
```