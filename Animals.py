import abc
import random

# Strategy Pattern: initialization
from EatStrategy import MessilyEatStrategy
from EatStrategy import DaintilyEatStrategy
from EatStrategy import FerociouslyEatStrategy
daintily_eat = DaintilyEatStrategy()
messily_eat = MessilyEatStrategy()
ferociously_eat = FerociouslyEatStrategy()

#base level
class Animal(object):
    __metaclass__ = abc.ABCMeta
    # name and eat strategy passed from subclass constructors
    def __init__(self, name, eat_strategy):
        self.name = name
        self._eat_strategy=eat_strategy

    @abc.abstractmethod
    def makeNoise(self):
        pass
    @abc.abstractmethod
    def roam(self):
        pass
    # Strategy Pattern: call passed eat strategy 
    def eat(self):
        print(self.name + self._eat_strategy.eat())
    def wakeUp(self):
        print(self.name + " woke Up!") 
    def sleep(self):
        print(self.name + " is going to sleep...") 

#type/roaming definitions (2nd level)
# Strategy Pattern: pass eat strategy to super constructor
class Canine(Animal):
    def __init__(self,name):
        super().__init__(name, ferociously_eat)
    def roam(self):
        print(self.name + " is roaming like a canine!")
class Feline(Animal):
    def __init__(self,name):
        super().__init__(name, daintily_eat)
    def roam(self):
        print(self.name + " is roaming like a feline!")
class Pachyderm(Animal):
    def __init__(self,name):
        super().__init__(name, messily_eat)
    def roam(self):
        print(self.name + " is roaming like a pachyderm!")

# individual animal definitions
#feline
class Cat(Feline):
    def __init__(self,name):
        self.randomAct = [" is sleeping...", " is roaming", " says MEOW!", daintily_eat.eat(), " is waking up!"]
        super().__init__(name+" the Cat")
        
    # call randomAction for random responses defines in randomAct
    def randomAction(self):
        randI = random.randint(0,4)
        print(self.name + self.randomAct[randI])
    def makeNoise(self):
        self.randomAction() 
    def wakeUp(self):
        self.randomAction()
    def eat(self):
        self.randomAction()
    def roam(self):
        self.randomAction() 
    def sleep(self):
        self.randomAction() 

class Tiger(Feline): 
    def __init__(self,name):
        super().__init__(name+" the Tiger")
    def makeNoise(self):
        print(self.name + " says rawr")
class Lion(Feline):
    def __init__(self,name):
        super().__init__(name+" the Lion")
    def makeNoise(self):
        print(self.name + " roars")

#canine
class Dog(Canine):
    def __init__(self,name):
        super().__init__(name+" the Dog")
    def makeNoise(self):
        print(self.name + " barks")
class Wolf(Canine):
    def __init__(self,name):
        super().__init__(name+" the Wolf")
    def makeNoise(self):
        print(self.name + " howls")
        
#pachyderm
class Elephant(Pachyderm):
    def __init__(self,name):
        super().__init__(name+" the Elephant")
    def makeNoise(self):
        print(self.name + " screams AAAAEEEEERRRRRRR")
class Rhino(Pachyderm):
    def __init__(self,name):
        super().__init__(name +" the Rhino")
    def makeNoise(self):
        print(self.name + " just grunts")
class Hippo(Pachyderm):
    def __init__(self,name):
        super().__init__(name +" the Hippo")
    def makeNoise(self):
        print(self.name + " says HUNGRY!")
