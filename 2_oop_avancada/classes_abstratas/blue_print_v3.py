import abc
from abc import ABC


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print("Welcome to Green Field")


class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()

# gera uma exception pois como não escrevemos o metodo hello a classe é considerada abstrata
rf = RedField()
