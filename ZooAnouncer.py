class ZooAnouncer:
    def __init__(self, Zookeeper, name="zooAnouncer"):
        self.name=name
        self.Zookeeper = Zookeeper
        # Observer Pattern: register self to object we are observing
        self.Zookeeper.register_observer(self)
        
    # Observer Pattern: method called by observable object to initiate some action(anounce)        
    def update(self):
        self.anounce()
        
    def anounce(self):
        print("Hi, this is the Zoo Announcer. The Zookeeper is about to wake the animals!")

    # Observer Pattern: deregister self from object we are observing
    def deRegister(self):
        self.Zookeeper.remove_observer(self)
    
    def __del__(self):
        print("zoo anouncer deconstructs")

