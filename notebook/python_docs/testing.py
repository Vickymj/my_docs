class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
print(obj.__private_var)   # ✗ AttributeError
print(obj.show_private())    # ✓ Access through method