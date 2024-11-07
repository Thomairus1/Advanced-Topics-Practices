from csv import reader

class Dog:
    def __init__(self, number, name, breed):
        self.name = name
        self.breed = breed
        self.number = number
        
    def __str__(self):
        return f"Number: {self.number}, Name: {self.name}, Breed: {self.breed}."

dogs = []

with open('dogs.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for number, name, breed in csv_reader:
        dogs.append(Dog(number, name, breed))

for dog in dogs:
    print(dog)
