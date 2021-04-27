prefix = '(From property)'

class Car:

    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]


@property
def make(self):
    return self.__make + prefix

@make.setter
def make(self, make):
    self.__make = make

@property
def model(self):
    return self.__model

@model.setter
def model(self, model):
    self.__model = model