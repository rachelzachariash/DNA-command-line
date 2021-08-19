from general.command import Command

'''
the class gets name of batch and save it in a file'''
class Batchsave(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    check if the input is valid and then 
    get the batch acceding to the name and get the string of all the command in the batch  and write it to the file
    '''
    def execute(self):
        if len(self.list_command)>=2 and len(self.list_command)<=3:
            if self.list_command[1][0]=='@':
                try:
                    object_observer=self.data_dna.get_batch_by_name(self.list_command[1][1:])
                    string_to_save = object_observer.get_command()
                except:
                    raise ValueError
                if len(self.list_command)==3:
                    file_name = self.list_command[2]
                else:
                    file_name = self.list_command[1][1:]+".txt"
                with open(file_name, "w") as f:
                    f.write(string_to_save)
            else:
                raise ValueError
        else:
            raise ValueError
