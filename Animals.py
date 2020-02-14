import abc
import random

#base level
class Animal(object):
    #per the lecture slides
    __metaclass__ = abc.ABCMeta
    def __init__(self, name):
        self.name = None;

    @abc.abstractmethod
    def wakeUp(self):
        return "waking up!!"
    def makeNoise(self):
        pass
    def eat(self):
        pass
    def roam(self):
        pass
    def sleep(self):
        return "going to sleep..." 

#type/roaming definitions (2nd level)
class Canine(Animal):
    def roam(self):
        return "Canine is roaming!"
class Feline(Animal):
    def roam(self):
        return "Feline is roaming!"
class Pachyderm(Animal):
    def roam(self):
        return "Pachyderm is roaming!"

# individual animal definitions
#feline
class Cat(Feline):
    def __init__(self,name):
        self.name = name
        
    # random cat actions defined individually
    def makeNoise(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 
    def wakeUp(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 
    def makeNoise(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 
    def eat(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 
    def roam(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 
    def sleep(self):
        randomAction = ["sleeping...", "roaming", "saying MEOW!", "eating fish", "waking up!"]
        randI = random.randint(0,4)
        return randomAction[randI] 

class Tiger(Feline): 
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "rawr"
class Lion(Feline):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "Roar"

#canine
class Dog(Canine):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "Woof"
class Wolf(Canine):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "Howl"
        
#pachyderm
class Elephant(Pachyderm):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "AAAAEEEEERRRRRRR"
class Rhino(Pachyderm):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "*grunt*"
class Hippo(Pachyderm):
    def __init__(self,name):
        self.name = name
    def makeNoise(self):
        return "HUNGRY!"
