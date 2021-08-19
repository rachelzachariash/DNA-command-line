
'''error class to if the string is not in type of DNA'''
class NotDnaString(Exception):


    def __init__(self):
        pass


    def __str__(self):
        return "DNA string as to consist only the letters A, C, T, G"
