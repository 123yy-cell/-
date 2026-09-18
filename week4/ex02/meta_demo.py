# 自定义元类：在类创建时打印信息
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"正在创建类: {name}")
        print(f"类属性: {list(attrs.keys())}")
        return super().__new__(cls, name, bases, attrs)

# 使用自定义元类创建类
class MyClass(metaclass=MyMeta):
    value = 100
    def hello(self):
        return "hello"

if __name__ == "__main__":
    obj = MyClass()
    print(f"类的类型: {type(MyClass)}")
    print(f"实例的类型: {type(obj)}")
