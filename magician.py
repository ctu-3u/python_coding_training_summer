from buffet import *

def show_magicians(magics):
    for item in magics:
        print(item.title())

def make_great(magics):
    great_magics = []
    for item in magics:
        item = "the Great " + item.title()
        great_magics.append(item)
    return great_magics        

magicians = ['lyney','lynette','freminet']
great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)

favorite_book("gone with the wind")