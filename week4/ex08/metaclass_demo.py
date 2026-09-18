class ValidateMeta(type):
    def __new__(cls, name, bases, attrs):
        # 强制校验：子类必须包含 name 属性
        if "name" not in attrs:
            raise TypeError(f"类 {name} 必须定义 name 属性")
        return super().__new__(cls, name, bases, attrs)

# 合法类：包含 name 属性
class GoodClass(metaclass=ValidateMeta):
    name = "demo"
    value = 10

if __name__ == "__main__":
    obj = GoodClass()
    print(f"类创建成功，name = {obj.name}")
