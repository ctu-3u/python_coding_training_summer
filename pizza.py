characters = ['alhaitham','nahida','furina','xianyun','lyney']
friend_characters = characters[:]
characters.append('gaming')
friend_characters.append('Sethos')

print("My favorite characters are")
for item in characters:
    print(item.title())
print("\nMy friend's favorite characters are")
for item in friend_characters:
    print(item.title())
