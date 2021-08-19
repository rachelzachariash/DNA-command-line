
import re

from general.command import Command
from general.dnaSequence import DnaSequence
'''
count how many times a dna sub string in a dna string'''

class Count(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    check that the input in valid id of name of DNA and sub string or id and DNA object
    and find all sub and print the len
    '''
    def execute(self):
        if len(self.list_command) == 3:
            my_string = self.check_dna(self.list_command[1]).get_string()
            if self.list_command[2][0] == '@' or self.list_command[2][0] == '#':
                my_sub_string = self.check_dna(self.list_command[2]).get_string()
            else:
                try:
                    my_sub_string = DnaSequence(self.list_command[2]).get_string()

                except:
                    raise ValueError
            my_index = re.findall(my_sub_string,my_string)
            if my_index == []:
                return "not find"
            return len(my_index)