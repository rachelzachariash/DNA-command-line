from DB.data import Data

'''
class that all the command inheritor from
-list_command the command split in to list
-data_dna the class of DB
-command the string of all the command
and function for help for a few command types
'''
class Command:

    def __init__(self, command):
        self.list_command = command.split(" ")
        self.data_dna = Data()
        self.command=command

    def get_command(self):
        return self.command

    def get_new_name(self,str,index):
        global new_name
        if self.list_command[index] == '@@':
            if self.list_command[1][0] == '@':
                new_name = self.data_dna.check_name(self.list_command[1][1:], str)
            else:
                name = self.data_dna.get_name_by_id(self.list_command[1][1:])
                new_name = self.data_dna.check_name(name, str)
        elif self.list_command[index][0] == '@':
            try:
                new_name = self.data_dna.check_name(self.list_command[index][1:], str)
            except IndexError:
                raise ValueError
        return new_name

    def write_data(self, new_name, id, dna_string):
        self.data_dna.push_dict(id, new_name, dna_string)

    def check_dna(self, seq):
        if seq[0] == '@':
            dict_name = self.data_dna.get_dict_name_id()
            try:
                name = seq[1:]
            except:
                raise ValueError
            if name in dict_name:
                dna_object = self.data_dna.get_dna_by_name(name)
            else:
                raise ValueError
        elif seq[0] == '#':
            dict_id = self.data_dna.dict_id_dna
            if seq[1:] not in dict_id:
                raise ValueError
            dna_object = self.data_dna.get_dna_by_id(seq[1:])
        else:
            raise ValueError
        return dna_object
    def execute(self):
        pass