# Composition is a class that exists inside of another class (class has a other class)

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    # For other programmers, for debugging. Tell class and all atributes
    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year}, {self.engine})"

class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def ignite(self):
        print("Vroom, vroom!")

    def __str__(self):
        return f"The engine is a {self.configuration} with {self.displacement} {self.horsepower} horsepower and {self.torque} torque."
    
    def __repr__(self):
        return f"Engine({self.configuration}, {self.displacement}, {self.horsepower}, {self.torque}.)"

myEngine = Engine("V8", 5.8, 326, 344)
myCar = Car("Mazda", "Mazda3", 2013, myEngine)

# To call a composite class you must access where it is saved within the class 
print(myCar)
myCar.engine.ignite()
print(repr(myCar))

print(repr(myEngine))