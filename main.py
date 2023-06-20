cars = ["Audi", "BMW", "Skoda", "Ford", "Mercedes"]
names = ["Travis", "Mari", "Ashley", "Fred", "Winston", "Sam", "Ben"]
cars.sort(key = lambda x: x.lower())
names.sort(key = lambda x: x.lower())
new_list = list(zip(names, cars))
print(new_list)
if len(names) > len(cars):
    print("Кому-то не достанется автомобиль")