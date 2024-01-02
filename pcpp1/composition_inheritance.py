'''
Estimated time
    45 minutes

Level of difficulty
    Medium

Objectives
    improving the student's skills in operating with inheritance and composition

Scenario
    Imagine that you are an automotive fan, and you are able to build a car from a
    limited set of components.

    Your task is to :
        define classes representing:
            tires (as a bundle needed by a car to operate); methods available:
            get_pressure(), pump(); attribute available: size
            engine; methods available: start(), stop(), get_state(); attribute available:
            fuel type
            vehicle; method available: __init__(VIN, engine, tires); attribute available:
            VIN
        based on the classes defined above, create the following objects:
            two sets of tires: city tires (size: 15), off-road tires (size: 18)
            two engines: electric engine, petrol engine
        instantiate two objects representing cars:
            the first one is a city car, built of an electric engine and city tires
            the second one is an all-terrain car build of a petrol engine and off-road tires
        play with the cars by calling methods responsible for interaction with
        components.
'''

class Vehicle:
    def __init__(self, vin, engine, tires) -> None:
        self.vin = vin
        self.engine = engine
        self.tires = tires

class Engine:
    def __init__(self, fuel_type) -> None:
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        print("Engine started")

    def stop(self):
        self.running = False
        print("Engine stopped")

    def get_state(self) -> bool:
        state = "started" if self.running else "stopped"
        print(f'The engine is {state}.')
        return self.running

class Tires:
    def __init__(self, size) -> None:
        self.size = size
        self.pressure = 0

    def get_pressure(self) -> float:
        print(f"Tire pressure: {self.pressure}")
        return self.pressure
    
    def pump(self, pressure):
        self.pressure = pressure

class City_Tires(Tires):
    def __init__(self) -> None:
        size = 15
        super().__init__(size)

class Off_Road_Tires(Tires):
    def __init__(self) -> None:
        size = 18
        super().__init__(size)

class Electric_Engine(Engine):
    def __init__(self) -> None:
        fuel_type = 'electric'
        super().__init__(fuel_type)

class Petrol_Engine(Engine):
    def __init__(self) -> None:
        fuel_type = 'petrol'
        super().__init__(fuel_type)

class City_Car(Vehicle):
    def __init__(self, vin) -> None:
        engine = Electric_Engine()
        tires = City_Tires()
        super().__init__(vin, engine, tires)

class All_Terrain_Car(Vehicle):
    def __init__(self, vin) -> None:
        engine = Petrol_Engine()
        tires = Off_Road_Tires()
        super().__init__(vin, engine, tires)

city_car = City_Car('4592343')
all_terrain_car = All_Terrain_Car('39403282')
city_car.tires.get_pressure()
city_car.tires.pump(100)
city_car.tires.get_pressure()
city_car.engine.get_state()
city_car.engine.start()
city_car.engine.get_state()
city_car.engine = Petrol_Engine()
city_car.engine.get_state()
city_car.engine.start()
city_car.engine.get_state()
