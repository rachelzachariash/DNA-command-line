from DB.data import Data
from general.command import Command

'''save in file dna according to the name or id'''
class Save(Command):
    def __init__(self, command):
        super().__init__(command)



    def write_to_file(self, dna, file):
        with open(file, 'w') as f:
            f.write(dna.get_string())

    def return_dna_name(self):
        if self.list_command[1][0] == '#':
            try:
                name = self.data_dna.get_name_by_id(self.list_command[1][1:]) + "​.rawdna"
                dna = self.data_dna.get_dna_by_id(self.list_command[1][1:])
                self.data_dna.change_sign_by_id(self.list_command[1][1:], '_')
            except:
                raise ValueError
        elif self.list_command[1][0] == '@':
            try:
                name = self.list_command[1][1:] + "​.rawdna"
                dna = self.data_dna.get_dna_by_name(self.list_command[1][1:])
                self.data_dna.change_sign_by_name(self.list_command[1][1:],'_')
            except IndexError:
                raise ValueError
        else:
            raise ValueError
        return [dna, name]
    '''check command is valid and check if file name as a suffix put in that file otherwise suffix is is .rawdna'''
    def execute(self):
        if len(self.list_command) == 2:
            dna_name = self.return_dna_name()
            self.write_to_file(dna_name[0], dna_name[1])
        elif len(self.list_command) == 3:
            dna_name = self.return_dna_name()
            self.write_to_file(dna_name[0], self.list_command[2])
        else:
            raise ValueError
        return "save complete"
