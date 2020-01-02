# -*- coding:utf-8 -*-


# # 经典单例模式
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#
# s = Singleton()
# print(s)
# s1 = Singleton()
# print(s1)
#
#
# # 单例模式的懒汉式实例化
# class Singleton:
#     __instance = None
#
#     def __init__(self):
#         if not Singleton.__instance:
#             print("__init__ method called..")
#         else:
#             print("Instance already created:", self.getInstance())
#
#     @classmethod
#     def getInstance(cls):
#         if not cls.__instance:
#             cls.__instance = Singleton()
#         return cls.__instance
#
#
# s = Singleton()
# print("Object created", Singleton.getInstance())
# s1 = Singleton()


# # Monostate单例模式， 通过init方法
# class Borg:
#     __shared_state = {"1": "2"}
#
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass
#
#
# b = Borg()
# b1 = Borg()
# b.x = 4
# print("Borg Object 'b': ", b)
# print("Borg Object 'b1': ", b1)
# print("Object State 'b1':", b1.__dict__)


# # Monostate单例模式，通过new方法
# class Borg:
#     __shared_state = {}
#
#     def __new__(cls, *args, **kwargs):
#         obj = super().__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls.__shared_state
#         return obj
#
#
# b = Borg()
# b1 = Borg()
# print("Borg Object 'b': ", b)
# print("Borg Object 'b1': ", b1)
# print("Object State 'b1':", b1.__dict__)


class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("*****Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)
