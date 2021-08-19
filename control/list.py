from general.command import Command

'''
return list of all the dna in the file
and the status where if they are saved or not'''
class List(Command):
    def __init__(self, command):
        super().__init__(command)
    '''
    create a string and append to it the next dna according to the id'''
    def execute(self):
        string=""
        keys_dict=self.data_dna.get_keys_id()
        keys_dict.sort()
        arr_sequence=self.data_dna.get_arr_by_id(keys_dict[0])
        dna=arr_sequence[0].get_string()
        if len(dna)>40:
            small_dna=dna[:40]
            dna=small_dna
        string_sequence="{} [{}] {}: {}".format(arr_sequence[2],keys_dict[0],arr_sequence[1],dna)
        string=string+string_sequence
        for i in keys_dict[1:]:
            arr_sequence = self.data_dna.get_arr_by_id(i)
            dna = arr_sequence[0].get_string()
            if len(dna) > 40:
                small_dna = dna[:40]
                dna = small_dna
            string_sequence = "\n{} [{}] {}: {}".format(arr_sequence[2], i, arr_sequence[1], dna)
            string = string + string_sequence
        return string

