import abc

# Abstract eat strategy
class EatStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def eat(self):
        """Required method"""

# Strategy Pattern: concrete implementtaions of eat strategy       
class DaintilyEatStrategy(EatStrategyAbstract):
    def eat(self):
        return (" daintily picks at the food")

class MessilyEatStrategy(EatStrategyAbstract):
    def eat(self):
        return (" is getting the food everywhere")

class FerociouslyEatStrategy(EatStrategyAbstract):
    def eat(self):
        return (" ferociously chows down")