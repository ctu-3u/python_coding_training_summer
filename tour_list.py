tour_list = ['Tromso','London','Nice','Rome','Berlin']
tour_list.sort()
print(tour_list)
tour_list.sort(reverse=True)
print(tour_list)
print(tour_list[-1])

characters = ['Sethos','Gaming','Chongyun','Xingqiu']
for character in characters:
    print(character + " is friend to Traveler.")

print("They are all friends to Traveler!")

numbers = [pow(value,3) for value in range(1,11)]
print(numbers)

print(sorted([9.4,0.4,5.4,0.2,5.5,0.0,12.3]))