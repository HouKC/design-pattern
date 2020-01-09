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

# 工厂方法模式
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create?[LinkedIn or Facebook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
