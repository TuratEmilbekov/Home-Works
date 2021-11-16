class Celebrity:
    def __init__(self, name, who, awards, car, wealth):
        self.name = name
        self.who = who
        self.awards =awards
        self.car = car
        self.wealth = wealth

    def star(self):
        return f'\n I am {self.name} and I\'ve won an award of {self.awards}\n'

    def relax(self):
        return f'\nI am {self.who}, rember my name\n'

    def __str__(self):
        return f'\nName: {self.name}\n' \
                f'\nWho: {self.who}\n' \
                f'\nAwards: {self.awards}\n' \
                f'\nCars: {self.car}\n' \
                f'\nWealth: {self.wealth}\n'

universe_1 = Celebrity(name='Eminem', who='King of Rap ("Mom\'s Spaghetti")', awards='has 25 Grammies and Artist of the Year, 2021', car='Lamborghini Hurricane, Mercedes A Class Sedan, Rolls-Royce Phantom', wealth='My Uncle')

# print('VivaLaVida' * 10)
# print(universe_1.star())
# print('VivaLaVida' * 10)
# print(universe_1.relax())
# print('VivaLaVida' * 10)
# print(universe_1)
# print('VivaLaVida' * 10)



class JackieChan(Celebrity):
    def how_it_started(self):
        return f'\nI am {self.name} and I have won {self.awards} in 2016 for my all films\n'

    def people(self):
        return f'\nMy biggest wealth is {self.wealth}\n'

    def __str__(self):
        return super(JackieChan, self).__str__()

universe_2 = JackieChan(name='Jackie Chan', who='Greatest Acttor Of All Time', awards='Academy Award', car='Lexus LX 600', wealth='My Family')

# print('diamond' * 10)
# print(universe_2.how_it_started())
# print('diamond' * 10)
# print(universe_2.people())
# print('diamond' * 10)
# print(universe_2)
# print('diamond' * 10)



class MichaelJordon(Celebrity):
    def way_to_the_sky(self):
        return f'My name is {self.name}, I\'m {self.who}'

    def goods(self):
        return f'I have a legendary Toyota car, {self.car}'

    def __str__(self):
        return super(MichaelJordon, self).__str__()

universe_3 = MichaelJordon(name='Michael Jordon', who='Greatest Basketball PLayer Of All Time', awards='Naismith Memorial Basketball Hall of Fame Class of 2009', car='Toyota GR Supra ', wealth='My Achivments')

# print('=' * 25)
# print(universe_3.way_to_the_sky())
# print('=' * 25)
# print(universe_3.goods())
# print('=' * 25)
# print(universe_3)
# print('=' * 25)



class Stars(MichaelJordon, JackieChan):
    def __str__(self):
        return super().__str__()

universe = Stars(name='Turat', who='Public personality', awards='World best actor', car='Ford Mustangs', wealth='Talent')

print('=' * 50)
print(universe.way_to_the_sky())
print('=' * 50)
print(universe.people())
print('=' * 50)
print(universe)
print('=' * 50)                          
                                
                                
                                
                                

#########################################################################################################################################################################


class Bilimkana:
    def __init__(self, name, location, director, salary_of_teacher, quantite_of_students, payment_for_study):
        self.name = name
        self.location = location
        self.director = director
        self.salary_of_teacher = salary_of_teacher
        self.quantite_of_students = quantite_of_students
        self.payment_for_study = payment_for_study

    def love_school(self):
        return f'My favourite school is {self.name}, its\'s located in {self.location}'

    def salary_for_teachers(self):
        return f'There we pay for a month around {self.salary_of_teacher}'

    def head(self):
        return f'Our director is {self.director}, he is owner of Facebook'

    def __str__(self):
        return f'\nName: {self.name}\n' \
                f'\nLocation: {self.location}\n' \
                f'\nDirector: {self.director}\n' \
                f'Salary: {self.salary_of_teacher}\n' \
                f'\nQuantite: {self.quantite_of_students}\n' \
                f'\nPayment: {self.payment_for_study}\n'

school_1 = Bilimkana(name='Bilimkana', location='Bishkek', director='Mark Suckerberg', salary_of_teacher='25 000$ per month', quantite_of_students=' 5000 students', payment_for_study='7000$ for a year')



class BilimkanaShabdan(Bilimkana):
    def location_place(self):
        return f'{self.name} located in {self.location}'

    def payment(self):
        return f'We pay for a month {self.payment_for_study}'

school_2 = BilimkanaShabdan(name='Bilimkana Shabdan', location='National park Chonkemin', director='Antony Banderas', salary_of_teacher='1000$ per month', quantite_of_students='2500 students', payment_for_study='1200$ per month')



class BilimkanaAmerican(Bilimkana):
    def story(self):
        return f'Our director bought Mr.{self.director} bought Whatsapp for 1 000 0000 000$, it\'s so sily, ahahahahhahaha'

    def school_day(self):
        return f'I give a present to my good, lika a school {self.name}'

school_3 = BilimkanaAmerican(name='Bilimkana American', location='Chyngyz Aitmatova st.', director="Turat TJ", salary_of_teacher='2500 $ per week', quantite_of_students='12 000 students', payment_for_study='25 000$ for a year')


class BilimkanaKant(Bilimkana):
    def salary_of_teachers(self):
        return f'If really say\'s they are took a {self.salary_of_teacher} per day'

    def payment_for_a_study(self):
        return f'Our guy\'s pay\'s around {self.payment_for_study}'

school_4 = BilimkanaKant(name='Bilimkana Kant', location="Kant- LUxemburg", director='Adam Seveni', salary_of_teacher='5000$ per month', quantite_of_students='25 000 students', payment_for_study='23 000$ per week')



#########################################################################################################################################################################

import random

class Cinema:
    def __init__(self, name, year, director_of_film, country, coast_of_ticket):
        self.name = name
        self.year = year
        self.director_of_film = director_of_film
        self.country = country
        self.coast_of_ticket = coast_of_ticket

    def __add__(self, others):
        if (isinstance(others, list)):
            others.append(self)
            return others
        else:
            return [self, others]
        
    def films(self):
        view_hall = random.randint(1, 6)
        return f'Today for all movies ticket will coast {self.coast_of_ticket}$, the movie will began in hall {view_hall}'

    def __str__(self):
        return f'\nName of movie: {self.name}\n' \
                f'\nYear of Issue: {self.year}\n' \
                f'\nDirector: {self.director_of_film}\n' \
                f'\nCountry: {self.country}\n' \
                f'\nCoast of movies: {self.coast_of_ticket}'

def selection(movie):
       for i in ListMovies:
           if i.name == movie:
               print(i.info())

Spider_Man = Cinema(name='Spider Man', year= 2021, director_of_film='John Watts',country='USA', coast_of_ticket='200 $')

Harry_Pooter = Cinema(name='Haryy Potter', year=2008, director_of_film='Chris Columbus', country='UK and USA', coast_of_ticket='500 $')

Forrest_Gump = Cinema(name='Forrest Gump', year= 1994, director_of_film='Robert Zemeckis', country='USA', coast_of_ticket='700 $')

Avengers = Cinema(name='Avengers', year= 2019, director_of_film='Anthony Russo and Joe Russo', country='USA', coast_of_ticket='1000 $')

Iron_Man = Cinema(name='Iron Man', year=2021, director_of_film='Shane Black and Jon Favreau', country='USA', coast_of_ticket='1500 $')

ListMovies = Spider_Man + Harry_Pooter
ListMovies = Forrest_Gump + ListMovies
ListMovies = Avengers + ListMovies
ListMovies = Iron_Man + ListMovies

Show = " "
for movie in ListMovies:
    print(movie)
    Show += movie.name + ", "

while 1:
    f = input(f'Select a movie \{Show}/: ')
    selection(f)
    if f == 'Exit':
        print('Exit')
        break

#########################################################################################################################################################################


class Starbucks:
    def __init__(self, branches, location, *names):
        self.branches = branches
        self.location = location
        self.names = []
        for i in names:
            self.names.append(i)

    def __len__(self):
        return len(self.names)

    def __add__(self, name):
        self.names.append(name)
        return self

    def __sub__(self, others):
        self.names.append(others)
        return self

    def NamesOfCoffee(self):
        print('Name Coffee')
        print('-' * 20)
        for name in self.names:
            if len(name) > 5:
                print(name, " - ", name[0:5])
            else:
                print(name, " - ", name)

    def NameOfCoffee(self, name):
        if len(name) > 5:
            print(name, " - ", name[0:5])
        else:
            print(name, " - ", name)


coffee = Starbucks('StraBucks AsiaMall', 'BishkekPark', 'Bilimkana')
print(len(coffee))

coffee = coffee + "Adilet"

coffee.NamesOfCoffee()

coffee.NameOfCoffee("Donald")