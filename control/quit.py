
from cli.confirm import Confirm
from general.command import Command

'''check if realy wants to quit the program'''
class Quit(Command):
    def __init__(self, command):
        super().__init__(command)
    '''send to the confirm cmd 
    checks how much dna is not save and modified and send it to the confirm start to print for the user'''
    def execute(self):
        confirm_quit = Confirm()
        amount_not_modified=0
        amount_new_sequences=0
        keys=self.data_dna.get_keys_id()
        for i in keys:
            arr_dna=self.data_dna.get_arr_by_id(i)
            if arr_dna[2]=='o':
                amount_new_sequences+=1
            elif arr_dna[2]=='*':
                amount_not_modified+=1
        string_write_command="There are {}​ modified ​and​ ​{}​ ​new​ sequences. Are you sure you want to quit?\n Please confirm by ​'y'​ ​or​ ​'Y'​, ​or​ cancel by ​'n'​ ​or​ ​'N'​. \n > confirm >>>".format(amount_not_modified,amount_new_sequences)
        user_confirm=confirm_quit.start(string_write_command)
        if user_confirm is True:
            return "Thank you ​for​ ​using​ Dnalanyzer.\n  Goodbye!"
        else:
            return "quit did not get confirm"