from cli.CLI import Cli

from batch.batch_controllers import Batch_controllers


# from factory import Factory
from error.Error_command import Error_command


class Batch_cmd(Cli):
    __instance = None
    '''singleton class'''
    def __new__(cls, *args, **kwargs):
        if not Batch_cmd.__instance:
            Batch_cmd.__instance = object.__new__(cls)
        return Batch_cmd.__instance
    '''
    observer- the command that the user insert will go into the observer 
    '''
    def __init__(self,class_observer):
        super().__init__()
        self.observer=class_observer

    '''
    get command until user insert end, 
    and send command to factory2
    to create the object'''
    def start(self,command):
        controller = Batch_controllers(self.observer)
        end=False
        while (not end):
            my_command = input(command)
            if my_command=='end':
                end=True
            else:
                try:
                    controller.get_object_observer(my_command)
                except ValueError:
                    print("command you insert not valid")
                except Error_command as err:
                    print(err)