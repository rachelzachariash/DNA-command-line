from general.command import Command
from general.dnaSequence import DnaSequence
'''create a new DNA'''

class New(Command):

    def __init__(self, command):
        super().__init__(command)
    '''create a dna accoding to the name that the user entered'''
    def execute(self):
        id = self.data_dna.get_id()
        if len(self.list_command) == 3:
            dna_string = DnaSequence(self.list_command[1])
            if self.list_command[2][0] != '@':
                raise ValueError
            try:
                new_name = self.list_command[2][1:]
            except IndexError:
                raise ValueError
            self.data_dna.push_dict(id, new_name, dna_string,'o')
        elif len(self.list_command) == 2:
            dna_string = DnaSequence(self.list_command[1])
            new_name = "str" + str(self.data_dna.get_no_name_given())
            self.data_dna.push_dict(id, new_name, dna_string,'o')
            self.data_dna.set_no_name_given()
        else:
            raise ValueError
        return "[{}] {}: {}".format(id, new_name, dna_string)
