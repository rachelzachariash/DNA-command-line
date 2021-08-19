from batch.factory2 import Factory2






class Batch_controllers:
    def __init__(self,observer):
        self.observer=observer
        self.my_factory = Factory2()

    def get_object_observer(self,command):
        self.my_factory.get_object_observer(command,self.observer)
