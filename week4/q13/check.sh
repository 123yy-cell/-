#!/usr/bin/env bash
set -e

echo "=== 检查代码格式 ==="
ruff format --check .

echo "=== 代码规范检查 ==="
ruff check .

echo "=== 运行单元测试 ==="
PYTHONPATH=src python3 -m pytest -v
