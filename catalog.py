class Engine:
    
    def __init__(self, engine_type, potency, weight):

        self.engine_type = engine_type
        self.potency = potency
        self.weight = weight

class Vehicle:
    def __init__(self,vehicle_type, chassis, model, gas_consumption, year, engine):
        self.vehicle_type = vehicle_type
        self.chassis = chassis
        self.model = model
        self.gas_consumption = gas_consumption
        self.year = year
        self.engine = engine

    def calculate_gas_consumption(self):
        chassis_factor= 0.3 if self.chassis == 'A' else 0.5 if self.chassis == 'B' else 0 
        return 1.1* self.engine.potency + 0.2 * self.engine.weight - chassis_factor
    
class Car(Vehicle):
    
    def __init__(self, chassis, model, gas_consumption, year, engine, num_doors):
        super().__init__('Car', chassis, model, gas_consumption, year, engine)
        self.num_doors = num_doors

class Truck(Vehicle):
    
    def __init__(self, chassis, model, gas_consumption, year, engine, payload_capacity):
        super().__init__('Truck', chassis, model, gas_consumption, year, engine)
        self.payload_capacity = payload_capacity

class Yacht(Vehicle):

    def __init__(self, chassis, model, gas_consumption, year, engine, length):
        super().__init__('Yacht', chassis, model, gas_consumption, year, engine)
        self.length = length

class Motorcycle(Vehicle):

    def __init__(self, chassis, model, gas_consumption, year, engine, num_wheels):
        super().__init__('Motorcycle', chassis, model, gas_consumption, year, engine)
        self.num_wheels = num_wheels


def display_vehicle_info(vehicle):
    print(f"Type: {vehicle.vehicle_type}")
    print(f"Chassis: {vehicle.chassis}")
    print(f"Model: {vehicle.model}")
    print(f"Year: {vehicle.year}")
    print(f"Gas Consumption: {vehicle.gas_consumption}")
    print(f"Engine Type: {vehicle.engine.engine_type}")
    print(f"Engine Potency: {vehicle.engine.potency}")
    print(f"Engine Weight: {vehicle.engine.weight}")

    if isinstance(vehicle, Car):
        print(f"Number of Doors: {vehicle.num_doors}")
    elif isinstance(vehicle, Truck):
        print(f"Payload Capacity: {vehicle.payload_capacity}")
    elif isinstance(vehicle, Yacht):
        print(f"Length: {vehicle.length}")
    elif isinstance(vehicle, Motorcycle):
        print(f"Number of Wheels: {vehicle.num_wheels}")

    print("\n")

# Ejemplo
engine1 = Engine('Gasoline', 200, 300)

car1 = Car('A', 'Sedan', 0, 2022, engine1, 4)
car1.gas_consumption = car1.calculate_gas_consumption()

truck1 = Truck('B', 'Pickup', 0, 2020, engine1, 1000)
truck1.gas_consumption = truck1.calculate_gas_consumption()

yacht1 = Yacht('A', 'Luxury', 0, 2023, engine1, 50)
yacht1.gas_consumption = yacht1.calculate_gas_consumption()

motorcycle1 = Motorcycle('B', 'Sport', 0, 2021, engine1, 2)
motorcycle1.gas_consumption = motorcycle1.calculate_gas_consumption()

# Mostrando información de cada tipo de vehículo 
display_vehicle_info(car1)
display_vehicle_info(truck1)
display_vehicle_info(yacht1)
display_vehicle_info(motorcycle1)

