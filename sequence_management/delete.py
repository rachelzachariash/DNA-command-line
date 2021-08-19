from cli.confirm import Confirm
from DB.data import Data

'''get a name or id and delete the dna'''
class Del:
    def __init__(self, command):
        self.__command = command
        self.list_command = command.split(" ")
        self.data_dna = Data()
    '''first get a confirm from the user if gat confirm check if command is valid and if yes delete form DB according to the name or id'''
    def execute(self):
        confirm_delete = Confirm()
        try:
            if self.list_command[1][0] == '#':
                name = self.data_dna.get_name_by_id(self.list_command[1][1:])
                dna = self.data_dna.get_dna_by_id(self.list_command[1][1:])

                string_to_confirm =  "Do you really want to {}: {}? Please confirm by ​'y'​ ​or​ ​'Y'​, ​or​ cancel by ​'n'​ ​or​ ​'N'​.".format( name, dna)
            elif self.list_command[1][0] == '@':
                name = self.list_command[1][1:]
                dna = self.data_dna.get_dna_by_name(self.list_command[1][1:])
                string_to_confirm="Do you really want to {}: {}? Please confirm by ​'y'​ ​or​ ​'Y'​, ​or​ cancel by ​'n'​ ​or​ ​'N'​.".format(name, dna)
            else:
                raise ValueError
        except:
            raise ValueError
        confirm_user = confirm_delete.start(string_to_confirm)
        if confirm_user:
            if len(self.list_command)==2:
                if self.list_command[1][0]=='#':
                    name = self.data_dna.get_name_by_id(self.list_command[1][1:])
                    dna = self.data_dna.get_dna_by_id(self.list_command[1][1:])
                    self.data_dna.delete_by_id(self.list_command[1][1:])
                    return "Deleted: [{}] {}: {}".format(self.list_command[1][1:],name, dna)
                elif self.list_command[1][0]=='@':
                    id = self.data_dna.get_dict_name_id()[self.list_command[1][1:]]
                    dna = self.data_dna.get_dna_by_name(self.list_command[1][1:])
                    self.data_dna.delete_by_name(self.list_command[1][1:])
                    return "Deleted: [{}] {}: {}".format(id, self.list_command[1][1:], dna)
                else:
                    raise ValueError
            else:
                raise ValueError

        else:
            return "delete dna did not get confirm"