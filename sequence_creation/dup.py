from general.command import Command
from general.dnaSequence import DnaSequence

'''get a id or name and gets the id and duplicate it and add new dna '''
class Dup(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
check if the command is valid and find the dna of the name of id that the user insert and add a new dna'''

    def execute(self):
        id = self.data_dna.get_id()
        if len(self.list_command)==3:
            if self.list_command[2][0]!='@':
                raise ValueError
            new_name = self.list_command[2][1:]
            dna_temp = self.check_dna(self.list_command[1])
            dna_string=DnaSequence(dna_temp.get_string() + dna_temp.get_string())
            self.data_dna.push_dict(id, new_name, dna_string,'o')
        elif len(self.list_command)==2:
            dna_temp = self.check_dna(self.list_command[1])
            dna_string = DnaSequence(dna_temp.get_string() + dna_temp.get_string())
            if self.list_command[1][0]=='@':
                new_name = self.data_dna.check_name(self.list_command[1][1:],'_')
            else:
                new_name=self.data_dna.check_name(self.data_dna.get_name_by_id(self.list_command[1][1:]),'_')
                self.data_dna.push_dict(id, new_name, dna_string,'o')
        else:
            raise ValueError
        return "[{}] {}: {}".format(id, new_name, dna_string)