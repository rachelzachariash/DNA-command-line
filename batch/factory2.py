
from error.Error_command import Error_command
from sequenceManipulation.pair import Pair
from sequenceManipulation.slice import Slice
from sequence_analysis.count import Count
from sequence_analysis.find import Find
from sequence_analysis.find_all import Find_all
from sequence_analysis.len import Len
from sequence_creation.dup import Dup
from sequence_creation.load import Load
from sequence_creation.new import New
from sequence_management.delete import Del
from sequence_management.save import Save

'''
a factory for creating a objects of command 
'''
class Factory2:
    def __init__(self):
        self.translations = {"count":Count,"new": New,"load": Load,"dup": Dup,"slice": Slice,"pair":Pair,"del": Del,"save":Save ,"find":Find,"findall":Find_all,"len":Len}

    '''
    each command that gets form the user in the batch cmd ceate a object according to the commad
    '''
    def get_object_observer(self, command,batch_observers):
        my_spliet_list = command.split(" ")
        command_type = my_spliet_list[0]
        if command_type in self.translations:
            execute_command = self.translations[command_type](command)
            batch_observers.attach(execute_command)
        else:
            raise Error_command(my_spliet_list[0])