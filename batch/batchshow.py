from general.command import Command

'''
print all the command in a batch
'''
class Batchshow(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    check input is valid 
    get the string of all the command and return it
    '''
    def execute(self):
        if len(self.list_command) == 2:
            if self.list_command[1][0] == '@':
                try:
                    observer_object = self.data_dna.get_observer_object(self.list_command[1][1:])
                except:
                    raise ValueError
                string_return = observer_object.get_command()
            else:
                raise ValueError

        else:
            raise ValueError
        return string_return