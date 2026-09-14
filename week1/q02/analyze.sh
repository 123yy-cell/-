#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file_path>" >&2
    exit 1
fi

csv_file="$1"

if [ ! -f "$csv_file" ]; then
    echo "Error: File '$csv_file' does not exist." >&2
    exit 1
fi

echo "Top 2 5xx paths:"
awk -F, 'NR > 1 && $4 >= 500 && $4 < 600 { cnt[$3]++ }
END {
    for (p in cnt) print cnt[p], p
}' "$csv_file" | sort -k1,1nr -k2,2 | head -n 2 | awk '{print $2}'

echo -e "\nAverage latency (ms):"
awk -F, 'NR > 1 { sum += $5; n++ }
END { printf "%.2f\n", sum / n }' "$csv_file"
