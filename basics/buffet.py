# current_users = ['admin','allen','alice','bob','charlie','daniel','eric']
# current_users_lower = [x.lower() for x in current_users]
# new_users = ['lily','lina','Alice','Bob','cathy']
# new_users_lower = [x.lower() for x in new_users]
# for new_user in new_users_lower:
#     if new_user in current_users_lower:
#         print("use another name.")
#     else:
#         print("welcome," + new_user + "!")


# learnt_words = {'insert':'Insert an item in a certain place of a list.',
#     'append':'Add one more item at the end of a list.',
#     'pop':'Pop out and delete the last item of a list.',
#     'remove':'Remoce the indicated item from a list.',
#     'del':'Delete something, like an item of a list.',
#     'sort':'Sort the list.',
#     'sorted':'Sort a lisr.',
#     'lower':'A string\'s lower case.',
#     'len':'Return length of a list.',}
# for [key, value] in learnt_words.items():
#     print(key + ": " + value)


# people = {
#     'alhaitham': {'name':'Alhaitham','age':'30','city':'Sumeru City','career':'scribe',},
#     'baizhu': {'name':'Baizhu','age':'30','city':'Liyue Harbor','career':'physician',},
#     'furina': {'name':'Furina','age':'500','city':'Fountain Court','career':'director',},
#     }
# for person, info in people.items():
#     print("\nCharacter: " + person)
#     print("Name: " + info['name'])
#     print("Location: " + info['city'])
#     print("Career: " + info['career'])

# favorite_numbers = {
#     'jean':[1,3.4,5],
#     'eula':[2,4,6],
#     'diluc':[7,8,9],
# }
# for name, number in favorite_numbers.items():
#     print(name.title() + "\'s favorite number(s) are:")
#     for num in number:
#         print(num)

# message = input("Anything you like:")
# message += " Cool!"
# print(message)

# number = int(input("Give me any number you are thinking of: "))
# if number % 10 == 0 :
#     print("WIn!")
# else:
#     print("Lose.")

# sandwich_orders = ['tuna','salmon','tuna','pastrami','salmon','chicken','chicken','egg','pastrami','pastrami','tuna','salmon','egg',]
# finished_sandwichies = []

# while sandwich_orders:
#     finished_sandwichies.append(sandwich_orders.pop())
#     print("I made your " + finished_sandwichies[-1] + " sandwich.")

# print("Pastrami sold out.")

# sandwich_orders = ['tuna','salmon','tuna','pastrami','salmon','chicken','chicken','egg','pastrami','pastrami','tuna','salmon','egg',]
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
# print(set(sandwich_orders))

def favorite_book(bookname):
    print("One of my favorite books is " + bookname.title() + ".")


def describe_city(cityname, countryname = 'switzerland'):
    print(cityname.title() + " is in " + countryname.title())


def make_sandwish(size, *ingredients):
    print("You ordered a " + size + " sandwich with ingredients:")
    for item in ingredients:
        print(item)


def make_car(brand,version,**style):
    car = {'brand':brand,'type':version,}
    for key, value in style.items():
        car[key] = value
    return car
