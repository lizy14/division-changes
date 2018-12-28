# 行政区划代码及变更整理步骤


## 1. 爬取历年行政区划变更文字说明
* `retrieve-descriptions.sh`
* 得到 `descriptions/source-b/1999.txt`

## 2. 爬取历年代码表 
* `retrieve-tables.sh`
* `parse-tables.py`
* 得到 `tables/1999.csv`

## 3. 比对相邻年的代码表
* `generate-diff.sh`
* 得到 `diffs/1999-2000.diff`

## 4. 根据比对结果生成规则
* `parse-diff.sh`
* 得到 `rules-generated/code-changes.csv`, `rules-generated/name-changes.csv`
* 匹配失败列表：`rules-generated/code-removals-unaccounted-for.log` 列出这样的代码，它们被删除了，但在当年新增代码中找不到对应的新代码

## 5. 人工核对
对照文字说明检查匹配失败列表，编写`rules-handwritten/code-merges.csv`, `rules-handwritten/code-splits.csv`

## 6. 大功告成
`translate.py`
