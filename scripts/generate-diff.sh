for i in $(seq 1980 2017); do 
    echo == $i ==; 
    diff --minimal $i.csv $((i+1)).csv > $i-$((i+1)).diff; 
done
