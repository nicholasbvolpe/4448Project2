from ZooAnouncer import ZooAnouncer
from Zookeeper import Zookeeper
from Animals import *
import sys

def main():
    # All animals at the zoo
    animals = []
    Henry = Hippo("Henry")
    animals.append(Henry)
    Harry = Hippo("Harry")
    animals.append(Harry)
    Edward = Elephant("Edward")
    animals.append(Edward)
    Elice = Elephant("Elice")
    animals.append(Elice)
    Ricky = Rhino("Ricky")
    animals.append(Ricky)
    Rachael = Rhino("Rachael")
    animals.append(Rachael)
    Tim = Tiger("Tim")
    animals.append(Tim)
    Tammy = Tiger("Tammy")
    animals.append(Tammy)
    Lucas = Lion("Lucas")
    animals.append(Lucas)
    Lucy  = Lion("Lucy")
    animals.append(Lucy)
    Carey  = Cat("Carey")
    animals.append(Carey)
    Coswald = Cat("Coswald")
    animals.append(Coswald)
    Wendy = Wolf("Wendy")
    animals.append(Wendy)
    Will = Wolf("Will")
    animals.append(Will)
    Dingo = Dog("Dingo")
    animals.append(Dingo)
    Darby = Dog("Darby")
    animals.append(Darby)

    Zookeep = Zookeeper()
    zooAnouncer = ZooAnouncer()
    Zookeep.register_observer(zooAnouncer)
    orig_stdout = sys.stdout
    
    Zookeep.wakeAnimals()
    
    for animal in animals:
        print(animal.name + " is " + animal.wakeUp())

    print("")
    
    Zookeep.rollCallAnimals()
    for animal in animals:
        print(animal.name + " says " + animal.makeNoise())
    

    print("")
    
    Zookeep.feedAnimals()
    for animal in animals:
        print(animal.name + " is eating!")
    
    print("")
    Zookeep.excerciseAnimals()
    for animal in animals:
        print(animal.name + " " + animal.roam())
    
    print("")
    Zookeep.shutdownZoo()
    for animal in animals:
        print(animal.name + " is " + animal.sleep())
    
    print("")
    f = open('./dayatthezoo.out', 'w')
    sys.stdout = f


if __name__ == "__main__":
    main()
    
