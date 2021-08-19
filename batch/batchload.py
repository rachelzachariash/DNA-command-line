from batch.factory2 import Factory2
from batch.batch_observers import Batch_observers
from general.command import Command

'''
get a name of file and load the file in to the batch
'''
class Batchload(Command):
    def __init__(self, command):
        super().__init__(command)

    '''
    get a name of file and add the end .txt
    checks if the name that the user insert start with a @
    if yes create with that name if the user didn't insert name the name is the file name
    read all the file in to a list (each line in a list)
    create a object type  batch_observer and for each line (command) create a object of the type of command and put it in
    in the new object batch_observer
    push the object in the DB
    '''
    def execute(self):
        if len(self.list_command) >= 2 and len(self.list_command) <= 3:
            file_name=self.list_command[1]+".dnabatch"
            if len(self.list_command) == 2:
                name=self.list_command[1]
            else:
                if self.list_command[2][0]=='@':
                    try:
                        name = self.list_command[2][1:]
                    except:
                        raise ValueError
                else:
                    raise ValueError
            try:
                with open(file_name,"r") as f:
                    arr_list=f.readlines()
            except:
                raise ValueError
            factory=Factory2()
            observer_batch = Batch_observers(name)
            for i in arr_list:
                factory.get_object_observer(i[:-1],observer_batch)
            self.data_dna.push_new_batch(name, observer_batch)
