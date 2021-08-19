from general.command import Command
from general.dnaSequence import DnaSequence

'''
find all the index of dna sub string in a dna string'''

class Find_all(Command):
    def __init__(self, command):
        super().__init__(command)

    '''
        check that the input in valid id of name of DNA and sub string or id and DNA object
        and check where index began if their a sub string and print the index
        '''
    def execute(self):
        if len(self.list_command) == 3:
            my_string=self.check_dna(self.list_command[1]).get_string()
            if self.list_command[2][0]=='@' or self.list_command[2][0]=='#':
                my_sub_string = self.check_dna(self.list_command[2]).get_string()
            else:
                try:
                    my_sub_string =DnaSequence(self.list_command[2]).get_string()
                except:
                    raise ValueError
            string_return=""

            index= my_string.index(my_sub_string,0)
            while index!=-1:
                string_return="{}{} ".format(string_return,index+1)
                try:
                    index = my_string.index(my_sub_string, index+1)
                except:
                    break
            if string_return=="":
                return "not find"
            # string_return=""
            # for i in my_index_array:
            #     string_return="{} {}".format(string_return,i)
            return string_return
        else:
            ValueError