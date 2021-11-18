class GetNumber:
    def __init__(self, numbers: list, desire_num: int):
        self.numbers = numbers
        self.desire_num = desire_num

    def index(self):
        for index_num in range(len(self.numbers)):
            for inx in range(index_num + 1, len(self.numbers)):
                if (self.numbers[index_num] + self.numbers[inx]) == self.desire_num:
                    return [index_num, inx]
        return None

    def __str__(self):
        return f'\nNumbers: {self.numbers}\n' \
            f'\nDesire number: {self.desire_num}\n'


numbers = GetNumber(numbers=[1, 2, 3, 5, 7, 8, 9, 11], desire_num=20)
print(numbers)
print(numbers.index())