class Human:
    name = 'Turat'
    age = 24
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def can_calculate(self, number_1, number_2):
        summary = number_1 + number_2
        return summary

    def can_win(self, football):
        champion = football
        return champion

    def can_say_hello(self):
        return 'Hello World'

    def __str__(self):
        return f'Name: {self.name}\n' \
            f'Age: {self.age}\n' \
            f'Height: {self.height}\n' \
            f'Gender: {self.gender}'


class Programmer(Human):
        def __init__(self, name, age, height, gender, language, fast_typing, logic_thinking):
            super().__init__(name, age, height, gender)
            self.language = language
            self.fast_typing = fast_typing
            self.logic_thinking = logic_thinking

        def can_freely_use_laptop(self):
            print('Yeap, I can freely use laptop like a Steve Jobs')

        def __str__(self):
            return super().__str__(), f'Language: {self.language}\n' \
                f'Fast_Typing: {self.fast_typing}\n' \
                f'Logic_Thinking: {self.logic_thinking}'



human_1 = Human(name= 'Turat', age= 17, height= 187, gender= 'Male')
human_2 = Human('Erzhan', 21, 183, 'Male')
print(human_1.can_say_hello())
print(human_1.can_calculate(int(input('first:')), int(input('second: '))))
print(human_1)
print(human_2)
proger = Programmer(language='Python', fast_typing=True, logic_thinking=True, 
                    name= 'Chontok', age= 20, height= 168, gender= 'Male')
print(proger)