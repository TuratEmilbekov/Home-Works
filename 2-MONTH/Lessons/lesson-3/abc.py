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
    def unl_call(self):
        return f'This number: {self.number}, can call but without restriction'

    def __str__(self):
        return super(UnlCallTarif,self).__str__()

number_2 = UnlCallTarif(name='Chontok', 
                number= '0777-558-885', 
                summary='2500 som')

print(number_2)
print('=' * 59)



class UnlInternetTarif(Tarif):
    def unl_internet(self):
        return f'Your internet package is unlimited'

    def __str__(self):
        return super(UnlInternetTarif, self).__str__()

number_3 = UnlInternetTarif(name='Chupapi', 
                number= '0777-885-558', 
                summary='5000 som')

print(number_3)
print('=' * 59)



class DiamondTarif(UnlInternetTarif, UnlCallTarif):
    def __str__(self):
        return super().__str__()

diamond = DiamondTarif(name='Chupapi', 
                            number= '0777-555-888', 
                            summary='12 000 som')

print(diamond.unl_call())
print(diamond.unl_internet())
print(diamond)


