from general.command import Command

'''
check len of DNA sequence'''

class Len(Command):
    def __init__(self, command):
        super().__init__(command)

    def execute(self):
        if len(self.list_command) == 2:
            my_string = self.check_dna(self.list_command[1])
            lenDna=len(my_string)
            return lenDna
        else:
            raise ValueError