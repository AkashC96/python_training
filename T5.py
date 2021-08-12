# Q1
print('Q1: ')
try:
    eval('a***a')
except SyntaxError:
    print("SyntaxError raised.")

# Q2
print('Q2: ')

import sys


def file(nam):
    try:
        if sys.argv[0] == nam:
            with open(nam, 'r') as f:
                f.read()
        raise FileExistsError("Enter file name again: ")

    except FileExistsError:
        raise


inp= input('Enter your file name:')
file(inp)

# Q3
print('Q3: ')


def four_digits(num):
    try:
        if num >= 10000:
            raise ValueError(num,' number is too long')
        elif num < 999:
            raise ValueError(nim,' number is too small')
        print(num)
    except:
        print('Onlly Enter Four digit number')
        raise

inp=int(input('Enter the number'))
four_digits(inp)


# Q4
print('Q4: ')
def login():
    username = input("enter username: ")
    password = input("enter password: ")
    password2 = input("re-enter your password: ")
    i=0
    while i<3:
        i=i+1
        if password == password2:
            print('Login Successful')
            break
        else:
            if i == 3:
                print('Maximum attempts reached!')
            else:
                print('Password does not match')
                password2=input('re-enter your password: ')

login()

# Q5
print('Q5: Completed task to understand finally and raise concept ')

# Q6
with open('doc.txt', 'w') as doc:
    doc.write("Hello I am a file\nWhere you need to return the data string\nwhich is of even length")
    doc.write('\nMake sure you return the same link as it is present')
with open('doc.txt', 'r') as doc:
    temp = ''
    for i in doc:
        temp = i.split()
        for j in temp:
            if len(j) % 2 == 0:
                temp=temp+" " + j

print(temp)
