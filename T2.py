#Q1
print('Q1')
X = int(input('Enter the number'))
print(X)

if X % 3 == 0:
    if X % 5 == 0:
        print('Consultadd - Python Training')
    else:
        print('Consultadd')
elif X % 5 == 0:
    print('Python Training')

#Q2
print('Q2')
x = int(input('Enter 1 for Addition\n 2 for Subtraction\n 3 for Division\n 4 for Multiplication\n 5 for Average'))

num1 = int(input('Enter First number'))
num2 = int(input('Enter Second number'))

if x == 1:
    y = num1+num2
elif x == 2:
    y = num1-num2
elif x == 3:
    if num1 > num2:
        y = num1 / num2
    else:
        y = num2 / num1
elif x == 4:
    y = num1 * num2
elif x == 5:
    num3 = int(input('Enter Third number'))
    num4 = int(input('Enter Fourth number'))
    y = (num1+num2+num3+num4)/4

print(y)
if y < 0:
    print('Negative')

#Q3
print('Q3')
a=10
b=20
c=30
avg=(a+b+c)/3
print('avg= ',avg)
if avg>a:
    if avg>b:
        if avg>c:
            print('avg is higher than a,b,c')
        else:
            print('avg is higher than a,b')
    elif avg>c:
        print('avg is higher than a,c')
    else:
        print('avg is higher than a')
elif avg>b:
        if avg>c:
            print('avg is higher than b,c')
        else:
            print('avg is higher than b')
elif avg>c:
    print('avg is higher than c')


#Q4
print('Q4')
x=1
while x>0:
    x=int(input('Enter the number'))
    if x>0:
        print('Good Going')
        continue
    else:
        print("It's Over")
        break


#Q5
print('Q5')
for x in range(2000,3200):
    if x % 7 ==0:
        if x % 5 != 0:
            print(x)


#Q6
print('Q6')
#1 = for i in x:
     #TypeError: 'int' object is not iterable

#2 = 0
    #error
    #1
    #error
    #2

#3 = 0
    #1
    #2
    #3
    #4


#Q7
print('Q7')
x=0
while(x<6):
    x=x+1
    if x!=3 and x!=6:
        print(x)
    else:
        continue


#Q8
print('Q8')
Sen=input('Enter string')
L=A=0
for x in Sen:
    if x.isdigit():
        L=L+1
    if x.isalpha():
        A=A+1

print("Number of letters: ", A)
print("Number of Numbers: ", L)


#Q9
print('Q9')
import random

Num = random.randint(1, 10)
Guess = 0

while Guess != Num:
    Guess = int(input("guess a number between 1 and 10: "))

    if Guess == Num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

#Q10
print('Q10')
i = 1
while i <=5:
    Guess = random.randint(1,10)
    Number= int(input("Guess the lucky number from 1 to 10: "))
    if Number == Guess:
        print("good guess")
    else:
        print("try again")
    if i == 5:
        print("game over")
    i +=1

#Q11
print('Q11')
i = 1
while i <=5:
    Guess = random.randint(1,10)
    Number= int(input("Guess the lucky number from 1 to 10: "))
    if Number == Guess:
        print("good guess")
        break
    else:
        print("try again")
    if i == 5:
        print("game over")
    i +=1