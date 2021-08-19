from general.command import Command
from general.dnaSequence import DnaSequence

'''pair a dna sequence according to id or name if their is : that make a new DNA
otherwise change on the id and name the DNA sequence'''
class Pair(Command):
    def __init__(self, command):
        super().__init__(command)



    def change_word(self,string):
        new_word=string
        string = ''
        for i in new_word:
            if i == 't' or i == 'T':
                string = string+'A'
            elif i == 'a' or i == 'A':
                string = string + 'T'
            elif i == 'c' or i == 'C':
                string = string + 'G'
            elif i == 'g' or i == 'G':
                string = string + 'C'
            else:
                raise ValueError
        return string

    def push_without_geting_name(self,id,index,dna_string):
        change_word = self.change_word(dna_string)
        if self.list_command[index] == ':':
            new_name = "str_{}".format(self.data_dna.get_no_name_given())
            self.data_dna.push_dict(id, new_name, DnaSequence(change_word),'o')
            return "[{}] {}: {}".format(id, new_name, change_word)
        else:
            raise ValueError
    '''
    check if command is valid
    find dna by id or name and pair it 
    it their no : in the command change the DNA sequence of the name or id
     otherwise if only : so create a new DNA
     and put a default name like str+no_name_seq if has name put in the new name
      if has @@ put in name old DNA with _num'''
    def execute(self):
        id = self.data_dna.get_id()
        dna_string = self.check_dna(self.list_command[1])
        if len(self.list_command)==2:
            change_word=self.change_word(dna_string)
            if self.list_command[1][0]=='@':
                self.data_dna.change_dna_by_name(dna_string,self.list_command[1][1:],"*")
                id=self.data_dna.get_dict_name_id()[self.list_command[1][1:]]
                new_name=self.list_command[1][1:]
            else:
                self.data_dna.change_dna_by_id(dna_string,self.list_command[1][1:],"*")
                id=self.list_command[1][1:]
                new_name=self.data_dna.get_name_by_id(self.list_command[1][1:])
            return "[{}] {}: {}".format(id, new_name, change_word)
        elif len(self.list_command) == 4:
            if self.list_command[2] == ':':
                change_word = self.change_word(dna_string)
                new_name = self.get_new_name('_p',3)
                self.data_dna.push_dict(id, new_name, DnaSequence(change_word),'o')
                return "[{}] {}: {}".format(id, new_name, DnaSequence(change_word))
            else:
                raise ValueError
        elif len(self.list_command) == 3:
            return self.push_without_geting_name(id,2,dna_string)
        else:
            raise ValueError







