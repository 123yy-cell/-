#!/usr/bin/env bash
set -e

# 拉取API数据，筛选后生成Markdown报告
curl -fsS http://127.0.0.1:8000/packages.json | jq -r '
  "# Package Summary",
  "",
  "| name | version | downloads |",
  "| --- | --- | --- |",
  (map(select(.status == "active" and .downloads >= 100))
   | sort_by([-.downloads, .name])
   | .[] | "| \(.name) | \(.version) | \(.downloads) |")
' > summary.md
