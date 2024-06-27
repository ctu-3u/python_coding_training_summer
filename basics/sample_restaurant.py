from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant('holy cow','burger')
icecreamstand = IceCreamStand('la cardia')

flavors = ['vanilla','chocolate','coffee','mint','mango','ram','strawberry','milk']
icecreamstand.record_flavors(flavors)
icecreamstand.show_flavors()
