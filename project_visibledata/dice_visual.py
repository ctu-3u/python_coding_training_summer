import pygal

from random_die import Die

 
die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(50000):
    result = die_1.throw_die()*die_2.throw_die()
    results.append(result)

frequencies = []
for value in range(1,65):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Multiplication of 2 dice of 8 faces"
hist.x_labels = list(range(1,65))
hist.x_title = "Result"
hist.y_title = "Frequency of Results"

hist.add('D8*D8',frequencies)
hist.render_in_browser()

