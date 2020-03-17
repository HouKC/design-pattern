# coding: utf8

# # 示例：编译器
# from abc import ABCMeta, abstractmethod
#
# class Compiler(metaclass=ABCMeta):
#     @abstractmethod
#     def collectSource(self):
#         pass
#
#     @abstractmethod
#     def compileToObject(self):
#         pass
#
#     @abstractmethod
#     def run(self):
#         pass
#
#     def compilerAndRun(self):
#         self.collectSource()
#         self.compileToObject()
#         self.run()
#
# class iOSCompiler(Compiler):
#     def collectSource(self):
#         print("Collecting Swift Source Code")
#
#     def compileToObject(self):
#         print("Compiling Swift code to LLVM bitcode")
#
#     def run(self):
#         print("Program running on runtime environment")
#
#
# iOS = iOSCompiler()
# iOS.compilerAndRun()

# # 简单例子
# from abc import ABCMeta, abstractmethod
#
# class AbstractClass(metaclass=ABCMeta):
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def operation1(self):
#         pass
#
#     @abstractmethod
#     def operation2(self):
#         pass
#
#     def template_method(self):
#         print("Defining the Algorithm. Operation1 follows Operation2")
#         self.operation2()
#         self.operation1()
#
#
# class ConcreteClass(AbstractClass):
#     def operation1(self):
#         print("My Concrete Operation1")
#
#     def operation2(self):
#         print("Operation 2 remains same")
#
# class Client:
#     def main(self):
#         self.concrete = ConcreteClass()
#         self.concrete.template_method()
#
#
# client = Client()
# client.main()


# 旅行社
from abc import ABCMeta, abstractmethod, ABC
class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")

    def day1(self):
        print("Appreciate Doge's Palace")

    def day2(self):
        print("Enjoy the food near the Rialto Bridge")

    def day3(self):
        print("Get souvenirs for friends and get back")

    def returnHome(self):
        pass

class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island, Wow!")

    def day1(self):
        print("Enjoy the marine life of Banana Reef")

    def day2(self):
        print("Go for the water sports and snorkelling")

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def returnHome(self):
        print("Don't feel like leaving the beach..")

class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


TravelAgency().arrange_trip()
