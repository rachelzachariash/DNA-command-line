from general.command import Command
from general.dnaSequence import DnaSequence


class Slice(Command):


    def __init__(self, command):
        super().__init__(command)


    def sub_dna(self,dna_string ,index_start,index_end):
        new_str_dna = ''
        if 0 <= int(index_start) < int(index_end )< len(dna_string):
            for i in range(int(index_start), int(index_end)):
                new_str_dna = new_str_dna + dna_string[i]
        return DnaSequence(new_str_dna)

    def check_type_insert(self):
        if len(self.list_command) < 4 and len(self.list_command)>6:
            raise ValueError
        dna_string = self.check_dna(self.list_command[1])

    '''
      check if command is valid
      find dna by id or name and slice it 
      it their no : in the command change the DNA sequence of the name or id
       otherwise if only : so create a new DNA
       and put a default name like str+no_name_seq if has name put in the new name
        if has @@ put in name old DNA with _num'''
    def execute(self):
        id = self.data_dna.get_id()
        dna_string = self.check_dna(self.list_command[1])
        if len(self.list_command) == 4:
            new_dna=self.sub_dna(dna_string,self.list_command[2],self.list_command[3])
            if self.list_command[1][0]=='@':
                self.data_dna.change_dna_by_name(new_dna,self.list_command[1][1:],"*")
                return "[{}] {}: {}".format(self.data_dna.get_dict_name_id()[self.list_command[1][1:]], self.list_command[1][1:], new_dna)
            else:
                self.data_dna.change_dna_by_id(new_dna, self.list_command[1][1:],"*")
                return "[{}] {}: {}".format(self.list_command[1][1:], self.data_dna.get_name_by_id(self.list_command[1][1:]),new_dna )
        elif len(self.list_command) == 5:
            new_dna = self.sub_dna(dna_string, self.list_command[2], self.list_command[3])
            if self.list_command[4]==':':
                new_name="str_{}".format(self.data_dna.get_no_name_given())
                self.data_dna.set_no_name_given()
                self.data_dna.push_dict(id, new_name, new_dna,"o")
                return "[{}] {}: {}".format(id, new_name, new_dna)
            else:
                raise ValueError
        elif len(self.list_command) == 6:
            new_dna = self.sub_dna(dna_string, self.list_command[2], self.list_command[3])
            new_name=self.get_new_name('_s',5)
            self.data_dna.push_dict(id, new_name, new_dna,'o')
            return "[{}] {}: {}".format(id, new_name, new_dna)
        else:
            raise ValueError












