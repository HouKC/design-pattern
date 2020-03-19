# coding:utf8

# # 简单示例
# from abc import abstractmethod, ABCMeta
# class State(metaclass=ABCMeta):
#     @abstractmethod
#     def Handle(self):
#         pass
#
# class ConcreteStateB(State):
#     def Handle(self):
#         print("ConcreteStateB")
#
# class ConcreteStateA(State):
#     def Handle(self):
#         print("ConcreteStateA")
#
# class Context(State):
#     def __init__(self):
#         self.state = None
#
#     def getState(self):
#         return self.state
#
#     def setState(self, state):
#         self.state = state
#
#     def Handle(self):
#         self.state.Handle()
#
#
# context = Context()
# stateA = ConcreteStateA()
# stateB = ConcreteStateB()
#
# context.setState(stateA)
# context.Handle()
# context.setState(stateB)
# context.Handle()

# # 状态设计模式具体实例：电视机开关
# from abc import abstractmethod, ABCMeta
# class State(metaclass=ABCMeta):
#     @abstractmethod
#     def doThis(self):
#         pass
#
# class StartState(State):
#     def doThis(self):
#         print("TV Switching ON..")
#
# class StopState(State):
#     def doThis(self):
#         print("TV Switching OFF..")
#
# class TVContext(State):
#     def __init__(self):
#         self.state = None
#
#     def getState(self):
#         return self.state
#
#     def setState(self, state):
#         self.state = state
#
#     def doThis(self):
#         self.state.doThis()
#
#
# context = TVContext()
# context.getState()
#
# start = StartState()
# stop = StopState()
#
# context.setState(stop)
# context.doThis()

# 状态设计模式具体实例：计算机系统开关机、休眠和挂起
class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, '=> switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, '=> switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name

class Off(ComputerState):
    name = "off"
    allowed = ['on']

class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']

class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ['on']

class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    comp = Computer()
    # State on
    comp.change(On)
    # Switch off
    comp.change(Off)
    # Switch on again
    comp.change(On)
    # Suspend
    comp.change(Suspend)
    # Try to hibernate - cannot!
    comp.change(Hibernate)
    # switch on back
    comp.change(On)
    # Finally off
    comp.change(Off)
