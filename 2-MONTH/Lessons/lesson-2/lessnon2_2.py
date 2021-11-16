class Panda:
    def __init__(self, name, weight, colour, fur):
        self.name = name
        self.weight = weight
        self.colour = colour
        self. fur = fur

    def style_kung_fu(self):
        style = f'\nDragon Warrior, because I\'m {self.name}\n'
        return style

    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Weight: {self.weight}\n' \
                f'Colour: {self.colour}\n' \
                f'Fur: {self.fur}'

panda = Panda(name='Poo', 
                weight='150 kg', 
                colour='Black and White', 
                fur=True)

print(panda)
print(panda.style_kung_fu())
print('=' * 32)



class Tiger:
    def __init__(self, name, weight, colour, fur):
        self.name = name
        self.weight = weight
        self.colour = colour
        self. fur = fur

    def style_kung_fu(self):
        style = f'\nTiger Style, because I\'m {self.name}\n'
        return style

    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Weight: {self.weight}\n' \
                f'Colour: {self.colour}\n' \
                f'Fur: {self.fur}'

tiger = Panda(name='Tigress',
                weight='70 kg',
                colour='Orange',
                fur=True)

print(tiger)
print(tiger.style_kung_fu())