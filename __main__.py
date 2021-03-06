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
    # Observer pattern: pass ZooAnouncer the observable object
    zooAnouncer = ZooAnouncer(Zookeep)

    # redirect output to file
    orig_stdout = sys.stdout
    f = open('./dayatthezoo.out', 'w')
    sys.stdout = f
    
    Zookeep.wakeAnimals()
    for animal in animals:
        animal.wakeUp()

    print("")
    
    Zookeep.rollCallAnimals()
    for animal in animals:
        animal.makeNoise()
    print("")
    
    Zookeep.feedAnimals()
    for animal in animals:
        animal.eat()
    
    print("")
    Zookeep.excerciseAnimals()
    for animal in animals:
        animal.roam()
    
    print("")
    Zookeep.shutdownZoo()
    for animal in animals:
        animal.sleep()

    zooAnouncer.deRegister()
    zooAnouncer.__del__()
    
    print("")
    # Return output to system out and close output file
    sys.stdout = orig_stdout
    f.close


if __name__ == "__main__":
    main()
    
