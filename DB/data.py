'''
the class hold all the DB
-id that is the amount of the dna that with insert
-no_name_given that give the num of the strings that was but in with out the a name
-dict_name_id a dict that has the name of a dna and the id
-dict_id_dna dict that the key is id of a dna and in the value list that the first place is dna and the name and third is the type whiere is the string
-dict_batch dict that contains key is name of batch and the value is a object of type of batch_observers
(and contains function to get the data)
'''

class Data(object):

    id=1
    __init=False
    no_name_given = 1
    __instance=None
    def __new__(cls, *args, **kwargs):
        if not Data.__instance:
            Data.__instance = object.__new__(cls)
        return Data.__instance

    def __init__(self):
        if  Data.__init==False:
            self.dict_name_id = {}
            self.dict_id_dna = {}
            self.dict_batch={}
            Data.__init=True
    def change_sign_by_name(self,name,sign):
        id=self.dict_name_id[name]
        arr=self.dict_id_dna[id]
        arr[2]=sign

    def change_sign_by_id(self, id, sign):
        arr = self.dict_id_dna[id]
        arr[2] = sign
    def get_batch_by_name(self,name):
        if name in self.dict_batch:
            return self.dict_batch[name]
        else:
            raise ValueError

    def get_name_batch(self):
        arr=[]
        for i in self.dict_batch:
            arr.append(i)
        return arr

    def get_dict_batch(self):
        return self.dict_batch

    def get_arr_by_id(self,id):
        return self.dict_id_dna[id]

    def get_keys_id(self):
        list_keys=[]
        for i in self.dict_id_dna:
            list_keys.append(i)
        return list_keys
    def push_new_batch(self,name,batch_object):
        self.dict_batch.update({name:batch_object})

    def check_name(self, name, str):
        dict_name = self.dict_name_id
        if name in dict_name:
            index = 1
            name = "{}{}{}".format(name, str, index)
            while name in dict_name:
                index += 1
                name = "{}{}{}".format(name[-2], str, index)
        return name

    def get_observer_object(self,name):
        if name in self.dict_batch:
            return self.dict_batch[name]
        else:
            raise ValueError

    def delete_by_id(self,id):
        name=self.dict_id_dna[str(id)][1]
        self.dict_id_dna.pop(str(id))
        self.dict_name_id.pop(name)

    def delete_by_name(self, name):
        id = self.dict_name_id[name]
        self.dict_id_dna.pop(str(id))
        self.dict_name_id.pop(name)

    def get_id(self):
        return Data.id

    def set_id(self):
        Data.id+=1

    def change_dna_by_name(self,dna,name,sign):
        self.dict_id_dna[self.dict_name_id[name]][0]=dna
        self.dict_id_dna[self.dict_name_id[name]][2] = sign

    def change_dna_by_id(self, dna, id,sign):
        self.dict_id_dna[str(id)][0] = dna
        self.dict_id_dna[str(id)][2] = sign

    def get_dna_by_id(self,id):
        return self.dict_id_dna[str(id)][0]

    def get_dna_by_name(self,name):
        id =self.dict_name_id[str(name)]
        return self.dict_id_dna[id][0]

    def push_dict(self,id,name,dna,sign):
        self.dict_id_dna.update({str(id):[dna,name,sign]})
        self.dict_name_id.update({name: str(id)})
        Data.id+=1

    def get_dict_id_dna(self):
        return self.dict_id_dna

    def get_dict_name_id(self):
        return self.dict_name_id

    def get_name_by_id(self,id):
        return self.dict_id_dna[str(id)][1]

    def set_no_name_given(self):
        Data.no_name_given+=1

    def get_no_name_given(self):
        return Data.no_name_given