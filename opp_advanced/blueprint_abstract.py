import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print("welcome to green field")


class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()
rf = RedField()