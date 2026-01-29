---
id: python_private_variables
title: Python - Private Variables
---

- **Public Variables:** Public variables are accessible from anywhere, both inside and outside the class
- **Protected Variables:** Protected variable can be accessed within the class and its subclasses.
- **Private Variables:** Private variables are only accessible within the class they are defined in. 

```py
class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# print(obj.__private_var)   # ✗ AttributeError
print(obj.show_private())    # ✓ Access through method
```

## Name Mangling for Private Variables
- private variables are not truly private. They can still be accessed from outside the class using a technique called name mangling.
- when you create a private variable using a double underscore (__var), Python internally changes its name to _ClassName__var. Now, you can access the private variable using this mangled name.
```py
class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# Accessing private variable using name mangling
print(obj._MyClass__private_var)  # ✓ Access using name mangling
```
