from random import randint

class Die():

    def __init__(self):
        self.value = randint(1,20)

    def throw_die(self):
        self.value = randint(1,20)

    def show_value(self):
        print(self.value)


die = Die()

i = 1
while i <= 20:
    die.throw_die()
    die.show_value()
    i += 1