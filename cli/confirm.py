from cli.CLI import Cli


class Confirm(Cli):
    __instance = None
    '''singleton class'''
    def __new__(cls, *args, **kwargs):
        if not Confirm.__instance:
            Confirm.__instance = object.__new__(cls)
        return Confirm.__instance

    def __init__(self):
        super().__init__()
    '''
    get the message to print to the user that hi should confirm
    and user need to insert Y or N
    '''
    def start(self,commad):
        cinfirm=False
        while cinfirm==False:
            my_command = input(commad)
            if my_command=='n' or my_command=='N':
                break
            elif my_command=='y' or my_command=='Y':
                cinfirm=True
        return cinfirm