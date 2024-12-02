class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        
        self.total_spots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric,
        }
        self.occupied_spots = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0,
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Adding a fuel vehicle of the specified fuel type.
        """
        if fuel_type not in self.total_spots:
            return False  
        if self.occupied_spots[fuel_type] < self.total_spots[fuel_type]:
            self.occupied_spots[fuel_type] += 1
            return True
        return False  

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Release a fuel slot of the specified fuel type.
        """
        if fuel_type not in self.total_spots:
            return False  
        if self.occupied_spots[fuel_type] > 0:
            self.occupied_spots[fuel_type] -= 1
            return True
        return False  



fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.fuel_vehicle("petrol"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.fuel_vehicle("electric"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.open_fuel_slot("diesel"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.open_fuel_slot("electric"))  
print(fuel_station.open_fuel_slot("electric"))  
