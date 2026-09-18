import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    """两个数相加"""
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
    print(f"函数名: {add.__name__}")
    print(f"文档字符串: {add.__doc__}")
