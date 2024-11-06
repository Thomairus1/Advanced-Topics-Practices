from csv import reader

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dogs = []

with open('dogs.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, breed in csv_reader:
        dogs.append(Dog(name, breed))

for dog in dogs:
    print(dog)