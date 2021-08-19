from general.command import Command

'''
get a name of a batch and run the batch
'''
class Run_batch(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    get the object according to name and notify the objects (execute all the command objects)
    '''
    def execute(self):
        if len(self.list_command) == 2:
            if self.list_command[1][0]=='@':
                try:
                    observer_object=self.data_dna.get_observer_object(self.list_command[1][1:])
                except:
                    raise ValueError
                string_return=observer_object.notify()
            else:
                raise ValueError
        else:
            raise ValueError
        return string_return