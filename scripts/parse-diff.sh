rm ../rules-generated/code-removals-unaccounted-for.log
rm ../rules-generated/code-changes.csv
rm ../rules-generated/name-changes.csv

(for year in $(seq 1984 2021); do
    python3 ./parse-diff.py ../diffs/$year-*.diff
done)
