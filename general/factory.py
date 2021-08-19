
from batch.batch import Batch
from batch.batchlist import Batchlist
from batch.batchload import Batchload
from batch.batchsave import Batchsave
from batch.batchshow import Batchshow
from batch.run_batch import Run_batch
from control.list import List
from control.quit import Quit
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
has a function get_localizer that gets a the command line 
that the user insert and create a class to deal with this command
and execute it'''

class Factory:
    def __init__(self):
        self.translations = {"quit":Quit,"list":List,"batchload":Batchload,"batchsave":Batchsave,"batchshow":Batchshow,"batchlist":Batchlist,"run":Run_batch,"batch":Batch,"count":Count,"new": New,"load": Load,"dup": Dup,"slice": Slice,"pair":Pair,"del": Del,"save":Save ,"find":Find,"findall":Find_all,"len":Len}

    def get_localizer(self, command):
        my_spliet_list = command.split(" ")
        command_type = my_spliet_list[0]
        if command_type in self.translations:
            execute_command= self.translations[command_type](command)
            print_back=execute_command.execute()
            return print_back
        else:
            raise Error_command(my_spliet_list[0])

    def get_object_observer(self, command,batch_observers):
        my_spliet_list = command.split(" ")
        command_type = my_spliet_list[0]
        if command_type in self.translations:
            execute_command = self.translations[command_type](command)
            batch_observers.attach(execute_command)
        else:
            raise Error_command(my_spliet_list[0])