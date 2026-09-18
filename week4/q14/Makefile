.PHONY: all clean

all: stats.txt report.txt

stats.txt: data.csv stats.py
	python3 stats.py

report.txt: report.md build_report.py stats.txt
	python3 build_report.py

clean:
	rm -f stats.txt report.txt
