from error.error_notDnaString import NotDnaString

'''
class for object of type DNA'''
class DnaSequence:
    validateLatter = ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']
    '''
    check if the dna is made of a,g,c,t latters'''
    @staticmethod
    def validate(string):
        if isinstance(string,str):
            for i in string:
                if i not in DnaSequence.validateLatter:
                    return False
            return True
        return False
    '''
    self.__string string Dna
    '''
    def __init__(self, string):
        if DnaSequence.validate(string):
            self.__string = string
        else:
            raise NotDnaString

    def get_string(self):
        return self.__string
    '''insert a new sub string'''
    def insert(self, sub_string, index):
        if 0 > index >= len(self.__string):
            raise ValueError("index out of range")
        if DnaSequence.validate(sub_string):
            self.__string = self.__string[:index] + sub_string + self.__string[index:]
        else:
            raise NotDnaString
    '''do a new object'''
    def assignment(self, other):
        if isinstance(other, DnaSequence):
            self.__string = object.get_string()
        elif DnaSequence.validate(other):
            self.__string = other
        else:
            raise NotDnaString

    def __str__(self):
        return self.__string

    '''check strings are equal'''

    def __eq__(self, other):
        if other.get_string == self.__string:
            return True
        return False

    '''check strings not equal'''
    def __ne__(self, other):
        if other.get_string == self.__string:
            return False
        return True
    '''get items in []'''
    def __getitem__(self, index):
        if 0 > int(index) >= len(self.__string):
            raise ValueError("index out of range")
        else:
            return self.__string[int(index)]

    '''set items in []'''
    def __setitem__(self, index, sub_string):
        if DnaSequence.validate(sub_string)==False:
            raise NotDnaString
        if 0 > index >= len(self.__string):
            raise NotDnaString
        if index == len(self.__string) - 1:
            self.__string = self.__string[:-1] + sub_string
        elif index == 0:
            self.__string = sub_string + self.__string[1:]
        else:
            self.__string = self.__string[:index] + sub_string + self.__string[index + 1:]
    '''get len'''
    def __len__(self):
        return len(self.__string)

