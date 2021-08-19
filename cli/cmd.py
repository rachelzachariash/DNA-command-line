from cli.CLI import Cli

from error.Error_command import Error_command
from error.error_notDnaString import NotDnaString
from general.factory import Factory


class Cmd(Cli):
    def __init__(self):
        super().__init__()

    '''
    user insert command and send it to the factory to create object in the type of command 
    '''
    def start(self,command):
        self.my_factory = Factory()
        quit=False
        while (quit is False):
            my_command = input(command)
            try:
                print_back = self.my_factory.get_localizer(my_command)
                if print_back is not None:
                    print(print_back)
                if print_back=="Thank you ​for​ ​using​ Dnalanyzer.\n  Goodbye!":
                    quit=True
            except ValueError:
                print("command you insert not valid")
            except Error_command as err:
                print(err)
            except NotDnaString as err:
                print(err)