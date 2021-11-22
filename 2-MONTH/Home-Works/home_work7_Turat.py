class OOP:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.numbers = [1, 21, 34, 657, 9876, 24, 235, 23]

    def bubble_sort(self):
        # replace = None
        for i in range(len(self.numbers) - 1, 0, -1):
            for j in range(i):
                if self.numbers [j] > self.numbers [j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
                    # replace = True
        #     if replace:
        #         replace = False
        #     else:
        #         break
        # return self.numbers



    

    def partition(self, nums):
        if len(nums) <= 1:
            return nums

        element = nums[0]
        left = list(filter(lambda num: num < element, nums))
        left = self.partition(left)
        center = [num for num in nums if num == element]
        right = list(filter(lambda num: num > element, nums))
        right = self.partition(right)

        return left + center + right

    def quick_sort(self):
        if len(self.numbers) <= 1:
            return self.numbers

        element = self.numbers[0]
        left = list(filter(lambda num: num < element, self.numbers))
        left = self.partition(left)
        center = [num for num in self.numbers if num == element]
        right = list(filter(lambda num: num > element, self.numbers))
        right = self.partition(right)

        return left + center + right
        


    def __str__(self):
        return f'numbers: {self.numbers} '



num = OOP(numbers=[1, 21, 34, 657, 9876, 24, 235, 23])
print(num)

print(num.bubble_sort())

# print(num.quick_sort())



##########################################################################################################################################################################################################################################################################################



def universal_number(number):
    number = str(number)
    for i in range (len(number) // 2):
        if number[i] != number [len(number) - 1 - i]:
            return False
    return True

num = universal_number(number= 343)
print(num)