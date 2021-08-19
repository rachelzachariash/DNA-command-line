class Error_command(Exception):
    '''error class if their no such command '''
    def __init__(self, command):
        self.command = command



    def __str__(self):
        return "no such command type as {}".format(self.command)
