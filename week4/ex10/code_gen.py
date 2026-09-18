# 自动生成多个 getter 函数模板
def generate_getters(properties):
    code = "# 自动生成的代码\n\n"
    for prop in properties:
        code += f"def get_{prop}(data):\n"
        code += f"    return data.get('{prop}')\n\n"
    return code

if __name__ == "__main__":
    props = ["name", "age", "email"]
    generated_code = generate_getters(props)
    # 写入生成的代码文件
    with open("generated.py", "w", encoding="utf-8") as f:
        f.write(generated_code)
    print("代码生成完成")
