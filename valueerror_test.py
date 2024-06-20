import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    break

    print("Give me two numbers, and I will add them together. \nType \'q\' to exit.")
    first_number = input("The first number is: ")
    if first_number == 'q':
        break
    second_number = input("The second number is: ")
    try:
        summa = float(first_number) + float(second_number)
    except ValueError:
        print("The input contains variable(s) that are not a number.")
    else:
        print("The summation is: ")
        print(summa)


# try:
#     with open('siddhartha.txt',encoding='utf-8') as siddhartha:
#         contents = siddhartha.read()
# except FileNotFoundError:
#     print("The file is not in this folder. Please check.\n")
# else:
#     the_times = contents.lower().count('the')
#     print("The time word \'the\' appears is " + str(the_times) + ".")


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = f_obj.read().strip('"')
    except FileNotFoundError:
        username = 'default'
    return username        


def get_new_username():
    username = input("Please type in the username you wanna use.")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if not username:
        username = get_new_username()
        print("Welcome, " + username + "!")
    else:
        while True:
            prompt = input("Is " + username + " your username? (yes/no)\nType in \'q\' to exit.")
            if prompt == 'yes':
                print("Welcome, " + username + "!")
                break
            elif prompt == 'no':
                username = get_new_username()
                print("Welcome, " + username + "!")
                break
            elif prompt == 'q':
                break


greet_user()