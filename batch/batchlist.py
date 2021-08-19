from general.command import Command

'''
return all the name of the batches in a list
'''
class Batchlist(Command):
    def __init__(self, command):
        super().__init__(command)
    def execute(self):
        if len(self.list_command)==1:
            return self.data_dna.get_name_batch()