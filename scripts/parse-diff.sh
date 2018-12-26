rm result/code-removals-unaccounted-for.log
rm result/code-changes.csv
rm result/name-changes.csv

(for year in $(seq 1984 2017); do 
    python ./parse-diff.py ./diffs/$year-*.diff 
done)
