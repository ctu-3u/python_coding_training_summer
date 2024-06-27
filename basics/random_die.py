from random import randint

class Die():

    def __init__(self,faces):
        self.value = randint(1,faces)
        self.faces = faces

    def throw_die(self):
        self.value = randint(1,self.faces)

    def show_value(self):
        print(self.value)

