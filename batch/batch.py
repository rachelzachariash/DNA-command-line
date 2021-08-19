from cli.batch_cmd import Batch_cmd
from batch.batch_observers import Batch_observers
from general.command import Command


class Batch(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    check if the command is in len of 2 and run the catch_cmd and save the new batch
    '''
    def execute(self):
        if len(self.list_command)==2:
            observer_batch=Batch_observers(self.list_command[1])
            batch_cmd=Batch_cmd(observer_batch)
            batch_cmd.start("> batch >>>")
            self.data_dna.push_new_batch(self.list_command[1],observer_batch)
        else:
            raise ValueError