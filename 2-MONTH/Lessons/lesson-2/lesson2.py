class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.language = language
        self. soft_skills = soft_skills
        self.laptop = laptop
        self. salary = salary

    def _say_which_language(self):
        return f'I am using {self.language}'

    def __str__(self):
        return f'Language: {self.language}\n' \
                f'Soft_skills: {self.soft_skills}\n' \
                f'Laptop: {self.laptop}\n' \
                f'Salary: {self.salary}'

junior_1 = Junior(language='Python', 
                    soft_skills='Good enough', 
                    laptop='Gaming laptop', 
                    salary= '300$')

print('=' * 50)
print(junior_1)



class MIddle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolvig, relyable):
        super().__init__(language, soft_skills, laptop, salary)
        self.fast_resolvig = fast_resolvig
        self.relyable = relyable

    def __str__(self):
        return super(MIddle, self).__str__() + f'\nFast_resolvig: {self.fast_resolvig}\n' \
                                                f'Relyable: {self.relyable}'     

middle1 = MIddle(language='Python', 
                    soft_skills='Good enough', 
                    laptop='Gaming laptop', 
                    salary= '7000$',
                    fast_resolvig='Often',
                    relyable=True)

print('=' * 50)
print(middle1)
print(middle1._say_which_language())



class Senior(MIddle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolvig, relyable, architecture, leading_skill):
        super().__init__(language, soft_skills, laptop, salary, fast_resolvig, relyable)
        self.architecture = architecture
        self.leading_skill = leading_skill

    def __str__(self):
        return super().__str__() + f'\nArchitecture: {self.architecture}\n' \
                                    f'Leading skill: {self.leading_skill}'

senior1 = Senior(language='Python', 
                    soft_skills='Good enough', 
                    laptop='Gaming laptop', 
                    salary= '10 000$',
                    fast_resolvig='Often',
                    relyable=True,
                    architecture=True,
                    leading_skill=True)

print('=' * 50)
print(senior1)
print('=' * 50)



