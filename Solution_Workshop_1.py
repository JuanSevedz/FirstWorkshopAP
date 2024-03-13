"""

"""

class Engine:
    """
    This class represents the engine an its qualyties 
    """
    def __init__(self, engine_type: str, potency: int, weight: float):

        self.engine_type = engine_type
        self.potency = potency
        self.weight = weight

class Vehicle:
    """
    This class representes the prymal class of all types of vehicles
    """
    def __init__(self, chassis:str, model:str, year: int, engine: Engine):
        if not chassis in ['A', 'B']:
            raise ValueError("This chassis is not valid.")


        self.chassis = None
        self.model = None
        self.gas_consumption = None
        self.year = None
        self.engine = None

    def _calculate_gas_consumption(self):
        consumption =((1.1* self.engine.potency) +
                      (0.2 * self.engine.weight)-
                      (0.3 if self.chassis == 'A' else 0.5))
        self.gas_consumption
    


class Car(Vehicle):
    """This class is a concrete definition for a car."""

class Truck(Vehicle):
    """This class is a concrete definition for a Truck"""
    
class Yacht(Vehicle):
    """This class is a concrete definition for a Yacht"""

class Motorcycle(Vehicle):
    """This class is a concrete definition for a Motorcycle"""


message = """
    Please, choose an option
    1. Crea
    2.
    3.
    4.
    5.
    6.
    7.
    8.

"""


def menu():
    print(message)
    option = 