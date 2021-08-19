from general.command import Command
from general.dnaSequence import DnaSequence

'''get id or name of dna and save it in a file'''
class Load(Command):
    def __init__(self, command):
        super().__init__(command)

    def good_file_name(self,name):
        if "." in name:
            return name
        return name+".rawdna"


    def get_dna(self,file_name):
        try:
            with  open(file_name, "r") as f:
                dna = f.read()
        except FileNotFoundError:
            raise ValueError
        return  DnaSequence(dna)


    def give_name(self,file_name):
        if "." not in file_name:
            return self.data_dna.check_name(file_name,'_')
        index=file_name.rfind(".")
        file_name=file_name[:index]
        return self.data_dna.check_name(file_name,'_')


    def validate_name(self,name):
        if len(name)>40:
            return name[:32]
        return name
    '''check if the command is valid and load the file and if their no name name is file name '''
    def execute(self):
        id = self.data_dna.get_id()
        if len(self.list_command)==3:
            try:
                if self.list_command[2][0]!='@':
                    raise ValueError
            except:
                raise ValueError
            new_name = self.validate_name(self.list_command[2][1:])
            file_name=self.good_file_name(self.list_command[1])
            dna_string = self.get_dna(file_name)
            self.data_dna.push_dict(id, new_name, dna_string,"-")
        elif len(self.list_command)==2:
            new_name=self.give_name(self.list_command[1])
            file_name = self.good_file_name(self.list_command[1])
            dna_string = self.get_dna(file_name)
            self.data_dna.push_dict(id, new_name, dna_string,"-")
        else: raise ValueError
        return "[{}] {}: {}".format(id, new_name, dna_string)


