import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


with open('guests.txt','a') as gl:
    while True:
        prompt = input("Please type in your name: \ntype in \'quit\' to quit. ")
        if prompt == 'quit':
            break
        print("Welcome, " + prompt.title())
        gl.write(prompt + "\n")