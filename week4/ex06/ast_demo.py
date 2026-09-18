import ast

code = """
def add(a, b):
    return a + b
"""

tree = ast.parse(code)

# 改写逻辑：把加法改成乘法
for node in ast.walk(tree):
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        node.op = ast.Mult()

# 编译并执行改写后的代码
exec(compile(tree, filename="<ast>", mode="exec"))
print(add(3, 4))
