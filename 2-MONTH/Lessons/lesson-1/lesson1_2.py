class Car:
    def __init__(self,brand, colour, type_car, amount_passengers, max_speed, engine, country, year, mechanic):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string!')

        if isinstance(colour, str):
            self.colour = colour
        else:
            raise ValueError('Colour should be string!')

        if isinstance(type_car, str):
            self.type_car = type_car
        else:
            raise ValueError('Type car should be string!')

        if isinstance(amount_passengers, int):
            self.amount_passengers = amount_passengers
        else:
            raise ValueError('Amount of passengers should be an integer!')

        if isinstance(max_speed, int):
            self.max_speed = max_speed
        else:
            raise ValueError('Max speed should be an integer!')

        if isinstance(engine, float):
            self.engine = engine
        else:
            raise ValueError('Engine should be float!')

        if isinstance(country, str):
            self.country = country
        else:
            raise ValueError('Country should be string!')

        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError('Year should be an integer!')

        if isinstance(mechanic, str):
            self.mechanic = mechanic
        else:
            raise ValueError('Mechanioc should be string!')

    def tunning(self, coast):
        car_coast = 5000
        summary = car_coast + coast
        return summary

    def __str__(self):
        return f'{self.brand}, {self.colour}, {self.amount_passengers}, {self.country}, {self.year}\n' \
            f'{self.max_speed}, {self.type_car}'

car_1 = Car(brand='BMW', colour='Black', type_car='Crossover', amount_passengers=4, max_speed=360, engine= 6.0, country='Germany', year=2021, mechanic='Nope')
print(car_1)
print(f'{car_1.tunning(80000)}$')
