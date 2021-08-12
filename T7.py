## Q1
print('Q1: prints the value according to the given formula')
C = 50
H = 30
D = input().split(',')
i =0
import math
while i < len(D):
    print(math.sqrt(2*C*int(D[i])/H))
    i += 1


## Q2
print('Q2: Shapes and square ')
class Shape:
    area = 0

    def getarea(self):
        print(self.area)

    class Square:
        def __init__(self, l):
            self.length = l

        def getarea(self):
            print(self.length * self.length)


sh = Shape()
sh.getarea()
sq = Shape.Square(4)
sq.getarea()


## Q3
print('Q3: class to find three elements that sum to zero from a set of n real numbers')
class GetNums:
    def __init__(self, nums):
        self.nums = nums

    def soln(self):
        l = len(self.nums)
        self.ans = []
        if l < 3:
            return []
        if l == 3:
            if sum(self.nums) == 0:
                return self.nums

        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                s = -(self.nums[i] + self.nums[j])
                if s in self.nums[j + 1:]:
                    self.ans.append([self.nums[i], self.nums[j], s])
        return self.ans


g = GetNums([-25, -10, -7, -3, 2, 4, 8, 10])
print(g.soln())


## Q4
print('Q4: Time class and initialize it with hours and minutes')
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


t1 = Time(1, 22)
t2 = Time(2, 50)


def addTime(t1, t2):
    hrs, mins = divmod(t1.minutes + t2.minutes, 60)
    return Time(t1.hours + t2.hours + hrs, mins)


def displayTime(t):
    print(str(t.hours) + ' hours and ' + str(t.minutes) + ' minutes')


def displayMinutes(t):
    print(str(t.hours * 60 + t.minutes) + ' minutes')


displayTime(addTime(t1, t2))
displayMinutes(addTime(t1, t2))


## Q5
print('Q5: Person class with an instance variable “age” and a constructor that takes an integer as a parameter ')
class Person:
    def __init__(self, i):
        if i >= 0:
            self.age = i
        else:
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def yearPasses(self, m):
        self.age += m
        return self.age

    def amIOld(self):
        if 0 <= self.age < 13:
            print('You are young.')
        elif 13 <= self.age <= 19:
            print('You are a teenager.')
        else:
            print('You are old.')


p = Person(4)
p.age
p.yearPasses(3)
p.amIOld()
p.yearPasses(10)
p.amIOld()
p.yearPasses(3)
p.amIOld()