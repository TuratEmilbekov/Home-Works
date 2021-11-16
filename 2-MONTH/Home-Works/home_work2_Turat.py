class Messi:
    def __init__(self, name, height, weight, working_foot, golden_ball, golden_boots):
        self.name = name
        self.height = height
        self.weight = weight
        self.working_foot =working_foot
        self.golden_ball = golden_ball
        self.golden_boots = golden_boots

    def champion(self):
        history_makers = f'\nMy name is {self.name}, I have won {self.golden_ball} and {self.golden_boots}\n'
        return history_makers

    def __str__(self):
        return  f'Name: {self.name}\n' \
                f'Height: {self.height}\n' \
                f'Weight: {self.weight}\n' \
                f'Worling foot: {self.working_foot}\n' \
                f'Golden ball: {self.golden_ball}\n' \
                f'Golden boots: {self.golden_boots}'

champ_1 = Messi(name='Lionel Messi', height= 1.72, weight= 70, working_foot='Left foot', golden_ball= '6 Golden Balls', golden_boots='6 Golden Boots')

print('=' * 70)
print(champ_1)
print(champ_1.champion())

class Ronaldo(Messi):
    def __init__(self, name, height, weight, working_foot, golden_ball, golden_boots, country, salary, cups):
        super().__init__(name, height, weight, working_foot, golden_ball, golden_boots)
        self.country = country
        self.salary = salary
        self.cups = cups

    def champion(self):
        history_makers = f'\nMy name is {self.name}, I have won {self.golden_ball} and {self.golden_boots}\n'
        return history_makers

    def __str__(self):
        return super().__str__() + f'\nCountry: {self.country}\n' \
                                    f'Salary: {self.salary}\n' \
                                    f'Cups: {self.cups}'

champ_2 = Ronaldo(name='Cristiano Ronaldo', height= 1.87, weight= 85, working_foot='Right foot', golden_ball= '5 Golden Balls', golden_boots='4 Golden Boots', country='Portugal', salary='1 billion per year', cups='38 cups')

print('=' * 70)
print(champ_2)
print(champ_2.champion())



class Neymar(Ronaldo):
    def __init__(self, name, height, weight, working_foot, golden_ball, golden_boots, country, salary, cups, cars, role_in_team, number):
        super().__init__(name, height, weight, working_foot, golden_ball, golden_boots, country, salary, cups)
        self.cars = cars
        self.role_in_team = role_in_team
        self.number = number 

    def champion(self):
        history_makers = f'\nMy name is {self.name}, I have won {self.golden_ball} and {self.golden_boots}\n'
        return history_makers

    def __str__(self):
        return super().__str__() + f'\nCars: {self.cars}\n' \
                                    f'Role in Team: {self.role_in_team}\n' \
                                    f'Number: {self.number}'

champ_3 = Neymar(name='Neymar Junior', height= 1.77, weight= 70, working_foot='Right foot', golden_ball= '3 Golden Balls', golden_boots='2 Golden Boots', country='Brazil', salary='3.5 billion per year', cups='28 cups', cars='Lamborghini', role_in_team='Captain', number=10)

print('=' * 75)
print(champ_3)
print(champ_3.champion())
print('=' * 70)



#########################################################################################################################################################################

class Education:
    def _math(self):
        print('Eto vnutrennii method ob6ecta')

study = Education()
study._math()
print('=' * 30)


class Education:
    def __init__(self):
        self.__math = 'Albert Einstein'


study = Education()
study.__math()



#########################################################################################################################################################################

class Barcelona:
    def champs(self):
        print('\nBuy Kun Aguero\n')

class ParisSaintGermain(Barcelona):
    def champs(self):
        print('\nSell\'s Cavani\n')

class ManchesterUnited(ParisSaintGermain):
    def champs(self):
        print('\nSack\'s Koeman\n')

maks = Barcelona()
maks.champs()

alex = ParisSaintGermain()
alex.champs()

ben = ManchesterUnited()
ben.champs()
print('=' * 70)



#########################################################################################################################################################################

class Naruto:
    def ninja(self):
        print('My main strenght Rasengan\n')

class Sasuke:
    def ninja(self):
        print('And I own a Sharingan')

class RockLee:
    def ninja(self):
        print('\nMy strongest attack is Youth Full Power\n')

anime_1 = Naruto()
anime_1.ninja()

anime_2 = Sasuke()
anime_2.ninja()


anime_3 = RockLee()
anime_3.ninja()