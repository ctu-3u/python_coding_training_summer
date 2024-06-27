banquet_list = []
banquet_list = ['Kylian Mbappe','Leo Messi','Christiano Ronaldo']
banquet_list[1] = 'Granit Xhaka'
    
banquet_list.insert(0,'Emilie')
banquet_list.insert(2,'Furina')
banquet_list.append('Navia')

for guest in banquet_list:
    print("\nI wanna invite " + guest + " to my banquet.")

sample_guests = banquet_list[0:3]
print("First three items are:")
print(sample_guests)
sample_guests = banquet_list[2:5]
print("Three items from the middle are:")
print(sample_guests)
sample_guests = banquet_list[-3:]
print("Last three items are:")
print(sample_guests)

