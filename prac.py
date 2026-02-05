# # # # # # # # # """
# # # # # # # # # Docstring for prac
# # # # # # # # # """
# # # # # from datetime import datetime

# # # # # # # # # # variables 

# # # # # # # # # name = "Vicky"
# # # # # # # # # is_name = True
# # # # # # # # # is_not_name = False
# # # # # # # # # age =30
# # # # # # # # # weight = 56.7


# # # # # # # # # print(f'Name={name}, {is_name=}')

# # # # # # # # # print(__doc__)
# # # # # # # # # print(name.split())
# # # # # # # # # name =name.replace("V", "B")
# # # # # # # # # print(name[0:3:2])
# # # # # # # # # print(round(weight,1))
# # # # # # # # # a = f"{weight:.2f}"
# # # # # # # # # print(a)
# # # # # # # # # a=2
# # # # # # # # # b=3
# # # # # # # # # print(a+b)
# # # # # # # # # print(a-b)
# # # # # # # # # print(a%b)
# # # # # # # # # print(a/b)
# # # # # # # # # print(a**b)
# # # # # # # # # print(a//b)


# # # # # # # # from sqlalchemy import true
# # # # # # # # from sqlmodel import desc


# # # # # # # # x, y = 10, 5
# # # # # # # # print(x>=y and x>0)
# # # # # # # # my_list = [0,1,2]
# # # # # # # # print(my_list)
# # # # # # # # my_list1 = list(range(0,6))
# # # # # # # # new_list = []
# # # # # # # # for seq in my_list1:
# # # # # # # #     new_list.append(seq *2)

# # # # # # # # new_list12 = [i**2 for i in my_list1]
# # # # # # # # print(new_list12)
# # # # # # # # new_list_map = list(map(lambda x: x*2,my_list1))
# # # # # # # # print(new_list_map)

# # # # # # # # print(new_list)
# # # # # # # # my_list = ['apple', 'banana', 'cherry']
# # # # # # # # another_list = ['fig', 'grape']
# # # # # # # # my_list[1] = "orange"
# # # # # # # # my_list.append("banana")
# # # # # # # # my_list.insert(0,"banana")
# # # # # # # # print(my_list+another_list)
# # # # # # # # my_list.extend(another_list)
# # # # # # # # my_list.remove("banana")
# # # # # # # # my_list.pop(1)
# # # # # # # # my_list.sort(reverse=True)
# # # # # # # # my_sortlist = sorted(my_list)
# # # # # # # # min(my_list)
# # # # # # # # my_name = "Vicky"
# # # # # # # # my_name_list = list(my_name)
# # # # # # # # my_name_list.sort()
# # # # # # # # print(my_name_list)
# # # # # # # # x = "".join(my_name_list)
# # # # # # # # print(x)
# # # # # # # # import random

# # # # # # # # print(random.choice([1,10]))
# # # # # # # # help(random.choice)


# # # # # # # # # print(
# # # # # # # # #     f"x > y and y > 0: {x > y and y > 0}, "  # True because both conditions are true
# # # # # # # # #     f"x > y or y < 0: {x > y or y < 0}, "    # True because at least one condition is true
# # # # # # # # #     f"not (x < y): {not (x < y)}"             # True because x < y is false
# # # # # # # # # )


# # # # # # # my_tuple = tuple(i for i in range(0,10))
# # # # # # # print(my_tuple)

# # # # # # # my_set = {1, 2, 3,3}
# # # # # # # my_set.add(5)
# # # # # # # my_set.clear()
# # # # # # # print(my_set)
# # # # # # # my_dict = {
# # # # # # #    "name" : "Vicky" ,
# # # # # # #    "age":20
# # # # # # # }
# # # # # # # del my_dict["name"]
# # # # # # # my_dict.popitem()

# # # # # # # # print(dict(name="vicky"))
# # # # # # # # print(my_dict.keys())
# # # # # # # # print(my_dict.values())
# # # # # # # # print(my_dict.items())
# # # # # # # # print(my_dict.get("name1"))
# # # # # # # # print()
# # # # # # # x=2
# # # # # # # while x>0:
# # # # # # #    print("ehllo")
# # # # # # #    x-=1

# # # # # # # name="helloworld"
# # # # # # # if 'h' in name:
# # # # # # #    print('YEs')
# # # # # # # for i in name:
# # # # # # #    print(i)

# # # # # # # for i in range(5):
# # # # # # #     print(i)
# # # # # # # else:
# # # # # # #     print("Loop is done")

# # # # # # # my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# # # # # # # print( my_dict.items())
# # # # # # # for i,key in enumerate(my_dict):
# # # # # # #     print(i,key)

# # # # # # # def testing_func(a:int=0,b:int=0)->int:
# # # # # # #     return a+b

# # # # # # # print(testing_func(b=1))


# # # # # # def new_func(*args, **kwargs):
# # # # # #    for arg in args:
# # # # # #       print(arg)
# # # # # #    for kw in kwargs:
# # # # # #       print(kw)

# # # # # # new_func(1,2,3,4,name="vicky")


# # # # # # my_list=[i for i in range(1,10)]
# # # # # # print(my_list)


# # # # # # new_list = list(filter(lambda x:x%2 ==0,my_list))
# # # # # # print(new_list)

# # # # # class User:
# # # # #    def __init__(self, name:str, age:int) -> None:
# # # # #         self.name=name
# # # # #         self.age=age
# # # # #    def get_user_name(self):
# # # # #        return self.name
# # # # #    def __repr__(self) -> str:
# # # # #        return f'User(name={self.name}, age={self.age})'




# # # # # class Student(User):
# # # # #    from datetime import datetime
# # # # #    year=datetime.now().time()
# # # # #    def __init__(self, name: str, age: int, dept:str) -> None:
# # # # #        super().__init__(name,age)
# # # # #        self.dept = dept
# # # # #    def get_user_name(self):
# # # # #        name = super().get_user_name()
# # # # #        return name.upper()
# # # # #    def __repr__(self) -> str:
# # # # #        return f"Student(name='{self.name}', age={self.age}, dept='{self.dept}'')"


# # # # # user1 = Student("vicky",28,'MECH')
# # # # # print(Student.year)
# # # # # print(f'{user1=}')
# # # # # print(f'{user1.get_user_name()=}')


# # # # from abc import ABC , abstractmethod

# # # # class User(ABC):
# # # #     @abstractmethod
# # # #     def get_user(self):
# # # #         pass
# # # #     def get_user_dept(self):
# # # #         pass
# # # # class Student(User):
# # # #     def get_user(self):
# # # #         pass
# # # #     def get_user_dept(self):
# # # #         pass
# # # #     def get_new_user(self):
# # # #         pass


# # # # student = Student()

# # # a = ["1","2"]
# # # print(''.join(a))

# # a= 1,2,3
# # tup = set(a)
# # print(tup.pop())
# # print('yes') if (1 in tup) else print('no')


# # class School:
# #     def __init__(self, name, accoutbalance):
# #         self.__name = name
# #         self.accoutbalance = accoutbalance

# #     @property
# #     def name(self):
# #         return f'account name: {self.__name}'
    
# #     @name.setter
# #     def name(self, new_name):
# #         self.__name = new_name

# #     @name.deleter
# #     def name(self):
# #         del self.__name 
    
# # s = School('a','345')
# # s.name="b"
# # print(s.accoutbalance)
# # del s.name
# # print(s.name)

# def dec_funct(func):
#     def wapper_func():
#         print("+++++")
#         func()
#         print("++++")
#     return wapper_func
# @dec_funct
# def main_func():
#     print("hello")

# main_func()


