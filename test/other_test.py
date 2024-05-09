import inspect
import os

class MyClass:
    def __init__(self):
        pass

    @staticmethod
    def some_method():
        data = inspect.stack()
        length = len(data)
        for _ in range(length):
            caller_frame = data[length-2]
            caller_name = caller_frame.function
            caller_class = caller_frame.frame.f_locals.get('self').__class__.__name__
            caller_filename = os.path.basename(caller_frame.filename)[:-3]
            caller_line_number = caller_frame.lineno
            if caller_class == 'MyClass':
                continue

            if caller_class == 'NoneType':
                print(f"[{caller_filename}.{caller_name}] [line {caller_line_number}]")
                break

            elif caller_class != 'NoneType':
                print(f"[{caller_filename}.{caller_class}.{caller_name}] [line {caller_line_number}]")
                break

    def info(self):
        self.some_method()

class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def test(self):
        self.obj.info()

def call():
    obj = MyClass()
    obj.info()

class Give:
    def __init__(self, obj):
        self.logger = obj

    def give(self):
        self.logger.info()



obj = AnotherClass()
obj.test()

d = MyClass()
d.info()

g = Give(d)
g.give()

call()
