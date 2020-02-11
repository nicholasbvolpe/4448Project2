class ZooAnouncer:
    def __init__(self, name="zooAnouncer"):
        self.name=name
        
    def update(self):
        self.Anounce()
        
    def Anounce(self):
        print("Hi, this is the Zoo Announcer. The Zookeeper is about to wake the animals!")