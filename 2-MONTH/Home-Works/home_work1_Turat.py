class Animal:
    def __init__(self, name, height, roar, color, country):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string!')

        if isinstance(height, float):
            self.height = height
        else:
            raise ValueError('Height should be float!')

        if isinstance(roar, str):
            self.roar = roar
        else:
            raise ValueError('Roar should be string!')

        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string!')

        if isinstance(country, str):
            self.country = country
        else:
            raise ValueError('Country should be string!')

    def __str__(self):
        return f'Animal name is {self.name}\n' \
            f'Animals height is {self.height}\n' \
            f'Animals roar is {self.roar}\n' \
            f'Animals color is {self.color}\n' \
            f'Animal from {self.country}'

animal_1 = Animal(name='Savanna Elephant', height= 3.2, roar='bahruuuuuuhhhhaaaaa', color='Grey', country='South AFRICA')
animal_2 = Animal(name='Amur Tiger', height= 1.20, roar='raaaayyyrrr', color='orange, white', country='Russia')
animal_3 = Animal(name='Giant Panda', height= 0.90, roar='uauauauuaaa', color='black, white', country='China')

# print(animal_1)
# print(animal_2)
# print(animal_3)

class Zoo(Animal):
    def __init__(self, name, height, roar, color, country, action, habitat, weight):
        super().__init__(name, height, roar, color, country)
        self.action = action
        if isinstance(action, str):
            self.action = action
        else:
            raise ValueError('Action should be string!')

        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError('Habitat should be string!')
        if isinstance(weight, str):
            self.weight = weight
        else:
            raise ValueError('Weight should be string!')

    def __str__(self):
        return super().__str__(), f'Animals action is {self.action}\n' \
                                f'Animals location is {self.habitat}\n' \
                                f'Animals weight is {self.weight}'

zoo_1 = Zoo(name='Savanna Elephant', height= 3.2, roar='bahruuuuuuhhhhaaaaa', color='Grey', country='South AFRICA', action='Somersault.', habitat='swimming pool and artificial savanna', weight='3 ton')
zoo_2 = Zoo(name='Amur Tiger', height= 1.20, roar='raaaayyyrrr', color='orange, white', country='Russia', action='Jumps through burning rings.', habitat='artificial forest', weight='3 ton')
zoo_3 = Zoo(name='Giant Panda', height= 0.90, roar='uauauauuaaa', color='black, white', country='China', action='Somersaults and will Scratches his tummy.', habitat='swimming pool and artificial savanna', weight='3 ton')



class Zoo_show:  
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0

        if (zoo.name == "Savanna Elephant"):
            self.ticket = '30$'
        if (zoo.name == "Amur Tiger"):
            self.ticket = '40$'
        if (zoo.name == "Giant Panda"):
            self.ticket = '50$'


    def tickete(self):
        return "Show will coast " + self.ticket

    def __str__(self):
        return f'{"=" * 50}\n' \
        f'{self.zoo.name} will show {self.zoo.action}'

eleph_show = Zoo_show(zoo_1)
eleph_show2 = Zoo_show(zoo_2)
eleph_show3 = Zoo_show(zoo_3)

print(eleph_show)
print(eleph_show.tickete())

print(eleph_show2)
print(eleph_show2.tickete())

print(eleph_show3)
print(eleph_show3.tickete())

input()