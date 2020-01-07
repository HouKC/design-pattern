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


# # 元类示例
# class MyInt(type):
#     def __call__(cls, *args, **kwargs):
#         print("*****Here's My int *****", args)
#         print("Now do whatever you want with these objects...")
#         return type.__call__(cls, *args, **kwargs)
#
#
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# i = int(4, 5)


# # 基于元类实现单例模式
# class MetaSingleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class Logger(metaclass=MetaSingleton):
#     pass
#
#
# logger1 = Logger()
# logger2 = Logger()
# print(logger1, logger2)

# # 单例模式示例：数据库读写操作
# import sqlite3
#
#
# class MetaSingleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class Database(metaclass=MetaSingleton):
#     connection = None
#
#     def connect(self):
#         if self.connection is None:
#             self.connection = sqlite3.connect("db.sqlite3")
#             self.cursorobj = self.connection.cursor()
#         return self.cursorobj
#
#
# db1 = Database().connect()
# db2 = Database().connect()
# print("Database Objects DB1", db1)
# print("Database Objects DB2", db2)


# 单例模式示例：运行状况监控服务
class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super().__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self.servers = []

    def addServer(self):
        self.servers.append("Server 1")
        self.servers.append("Server 2")
        self.servers.append("Server 3")
        self.servers.append("Server 4")

    def changeServer(self):
        self.servers.pop()
        self.servers.append("Server 5")


hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1.servers[i])
hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2.servers[i])
