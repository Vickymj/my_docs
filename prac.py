# def func():
#     """
#     Hello dear
#     """
# print(func.__doc__)
# print(__name__)
# from collections import Counter

# a= Counter([1,2,3,1,2,3])
# print(a)


def outerfunc(val):
    data = "vanl"
    def innerfunc():
        print(data)
    return innerfunc

vasdlf  = outerfunc("a")
vasdlf()