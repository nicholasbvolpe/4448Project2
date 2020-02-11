class Zookeeper:
    def __init__(self, name="zookeeper"):
        self.name = name
        self.observers= []
    
    def register_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def wakeAnimals(self):
        print("The zookeeper begins shaking the animals awake")
        self.notify_observers()

    def rollCallAnimals(self):
        print("The zookeeper starts roll Calling animals")

    def feedAnimals(self):
        print("The Zookeeper feeds all the animals pizza")

    def excerciseAnimals(self):
        print("The zookeeper gets out his coaching whistle and excercises the animals")

    def shutdownZoo(self):
        print("The zookeeper locks the gate and reads the animals a bedtime story")
