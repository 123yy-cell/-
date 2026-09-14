import argparse
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    
    # name 去除首尾空白后为空则退出，退出码为 2
    if not a.name.strip():
        sys.exit(2)
    
    print(f"Hello, {a.name}!")
