from ZooAnouncer import ZooAnouncer
from Zookeeper import Zookeeper
import sys

def main():
    # All animals at the zoo
    animals = []
    """ animals[0] = new Hippo("Henry")
    animals[1] = new Hippo("Harry")
    animals[2] = new Elephant("Edward")
    animals[3] = new Elephant("Elice")
    animals[4] = new Rhino("Ricky")
    animals[5] = new Rhino("Rachael")
    animals[6] = new Tiger("Tim")
    animals[7] = new Tiger("Tammy")
    animals[8] = new Lion("Lucas")
    animals[9] = new Lion("Lucy")
    animals[10] = new Cat("Carey")
    animals[11] = new Cat("Coswald")
    animals[12] = new Wolf("Wendy")
    animals[13] = new Wolf("Will")
    animals[14] = new Dog("Dingo")
    animals[15] = new Dog("Darby") """

    Zookeep = Zookeeper()
    zooAnouncer = ZooAnouncer()
    Zookeep.register_observer(zooAnouncer)
    orig_stdout = sys.stdout
    
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
    
    print("")
    f = open('./dayatthezoo.out', 'w')
    sys.stdout = f


if __name__ == "__main__":
    main()
    
