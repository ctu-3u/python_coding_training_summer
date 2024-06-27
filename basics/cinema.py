while True:
    prompt = input("Your age is: \nEnter 'quit' to end the program.")
    if prompt == 'quit':
        break
    else:
        prompt = int(prompt)
    if prompt < 3:
        price = 0
    elif prompt >= 3 and prompt <= 12:
        price = 10
    else:
        price = 15
    print("The price is: " + str(price))
