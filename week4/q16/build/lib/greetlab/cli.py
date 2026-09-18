import sys


def main():
    # 解析 --name 参数
    arg_list = sys.argv[1:]
    name = ""
    if "--name" in arg_list:
        pos = arg_list.index("--name")
        if pos + 1 < len(arg_list):
            name = arg_list[pos + 1]

    # 空白姓名以退出码 2 退出
    name = name.strip()
    if not name:
        sys.exit(2)

    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
