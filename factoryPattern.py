# -*- coding:utf-8 -*-

# # 简单工厂模式（森林动物猫狗叫）
# from abc import ABCMeta, abstractmethod
#
#
# class Animal(metaclass=ABCMeta):
#     @abstractmethod
#     def do_say(self):
#         pass
#
#
# class Dog(Animal):
#     def do_say(self):
#         print("Bhow Bhow!!")
#
#
# class Cat(Animal):
#     def do_say(self):
#         print("Meow Meow!!")
#
#
# # forest factory defined
# class ForestFactory(object):
#     def make_sound(self, object_type):
#         return eval(object_type)().do_say()
#
#
# # client code
# if __name__ == '__main__':
#     ff = ForestFactory()
#     animal = input("Which animal should make sound Dog or Cat?")
#     ff.make_sound(animal)

# # 工厂方法模式
# from abc import ABCMeta, abstractmethod
#
#
# class Section(metaclass=ABCMeta):
#     @abstractmethod
#     def describe(self):
#         pass
#
#
# class PersonalSection(Section):
#     def describe(self):
#         print("Personal Section")
#
#
# class AlbumSection(Section):
#     def describe(self):
#         print("Album Section")
#
#
# class PatentSection(Section):
#     def describe(self):
#         print("Patent Section")
#
#
# class PublicationSection(Section):
#     def describe(self):
#         print("Publication Section")
#
#
# class Profile(metaclass=ABCMeta):
#     def __init__(self):
#         self.sections = []
#         self.createProfile()
#
#     @abstractmethod
#     def createProfile(self):
#         pass
#
#     def getSections(self):
#         return self.sections
#
#     def addSections(self, section):
#         self.sections.append(section)
#
#
# class linkedin(Profile):
#     def createProfile(self):
#         self.addSections(PersonalSection())
#         self.addSections(PatentSection())
#         self.addSections(PublicationSection())
#
#
# class facebook(Profile):
#     def createProfile(self):
#         self.addSections(PersonalSection())
#         self.addSections(AlbumSection())
#
#
# if __name__ == '__main__':
#     profile_type = input("Which Profile you'd like to create?[LinkedIn or Facebook]")
#     profile = eval(profile_type.lower())()
#     print("Creating Profile..", type(profile).__name__)
#     print("Profile has sections --", profile.getSections())

# 抽象工厂模式
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):      # 抽象披萨工厂类
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndiaPizzaFactory(PizzaFactory):      # 印式披萨工厂类
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):     # 美式披萨工厂类
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):      # 抽象素菜披萨类
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):   # 抽象非素菜披萨类
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):       # 多彩披萨类
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):    # 鸡肉披萨类
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):    # 墨西哥披萨类
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):        # 汉姆披萨类
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:           # 披萨店，即客户端
    def __init__(self):
        pass

    def makePizzas(self):   # 制作披萨，根据需求实例化工厂，选择调用工厂的接口制作素菜或者非素菜披萨
        for factory in [IndiaPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()    # 实例化客户端
pizza.makePizzas()
