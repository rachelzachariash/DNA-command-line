
'''
class for the type of each batch
-_observers a list of object of command etc New Count Save(all the command that in the batch)
-name name of command
'''


class Batch_observers:
    def __init__(self,name):
        self._observers = []
        self.name=name
    '''
    execute (run) all of the object in the list observer 
    and make a string to return to the user of all of the result of the command that runed
    '''
    def notify(self, modifier=None):
        string_return=""
        for observer in self._observers:
            if modifier != observer:
                try:
                    return_value=observer.execute()
                    if string_return == "":
                        string_return = string_return + return_value
                    else:
                        string_return=string_return+"\n"+return_value
                except:
                    if string_return == "":
                        string_return = string_return + "\n" + "command faild"
                    else:
                        string_return=string_return+"\n"+"command faild"
        return string_return
    '''
    add a new object to the observer
    '''
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    '''
      delete a object from the observer
      '''
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    '''
    get all of the string command
    for each object in the observer get the command line string 
    '''
    def get_command(self):
        string_return = ""
        for observer in self._observers:
            return_value = observer.get_command()
            if string_return=="":
                string_return = string_return +return_value
            else:
                string_return = string_return + "\n" + return_value
        return string_return

