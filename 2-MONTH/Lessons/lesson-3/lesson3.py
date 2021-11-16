class Tarif:
    def __init__(self, number, name, summary):
        self.number = number 
        self.name = name
        self.summary = summary

    def call(self):
        return f'This number: {self.number}, can call but with restriction'

    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Number: {self.number}\n' \
                f'Summary: {self.summary}'


number_1 = Tarif(name='Erzhan', 
                number= '0777-557-885', 
                summary='120 som')
print(number_1)
print('=' * 35)



class UnlCallTarif(Tarif):
    def __init__(self, number, name, summary, coast):
        super().__init__(number, name, summary)
        self.coast = coast

    def unl_call(self):
        return f'This number: {self.number}, can call but without restriction'

    def __str__(self):
        return super(UnlCallTarif, self).__str__() + f'\nCoast: {self.coast}'

number_2 = UnlCallTarif(name='Chontok', 
                        number= '0777-557-775', 
                        summary='1500 som', 
                        coast=200)
print(number_2)
print('=' * 35)



class UnlInternetTarif(Tarif):
    def __init__(self, number, name, summary, internet_package):
        super().__init__(number, name, summary)
        self.internet_package = internet_package

    def unl_internet(self):
        return f'Your internet package is unlimited'

    def __str__(self):
        return super(UnlInternetTarif, self).__str__() + f'\nInternet Package: {self.internet_package}'

number_3 = UnlInternetTarif(name='Kucha', 
                            number= '0777-555-555', 
                            summary='4000 som',  
                            internet_package='unlimited')
print(number_3)
print('=' * 35)



class DiamondTarif(UnlInternetTarif, UnlCallTarif):
    def __init__(self, number, name, summary, internet_package):
        super().__init__(number, name, summary, internet_package)

    def __str__(self):
        return super(DiamondTarif, self).__str__()

diamond = DiamondTarif(name='Chupapi', 
                            number= '0777-555-888', 
                            summary='12 000 som',  
                            internet_package='unlimited')


diamond.unl_call()
diamond.unl_internet()
diamond.call()      

print(diamond)


# БЫЛА ОШИБКА НА ЭТОМ КОДЕ, ИЗ-ЗА ЭТОГО Я СОЗДАЛ ДРУГОЙ ПИТОН-ФАЙЛ