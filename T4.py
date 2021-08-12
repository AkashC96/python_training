# Q1
print('Q1: reverse a string.')
string = input('Enter String :')
B = []
for i in range(1, len(string) + 1):
    B.append(string[-i])
print('Reverse String:', ''.join(B))

# Q2
print('Q2: prints the number of uppercase letters and lowercase')


def upperandlowercount():
    string2 = input('Enter String :')
    U = 0
    L = 0
    for i1 in string2:
        if i1.isupper():
            U = U + 1
        elif i1.islower():
            L = L + 1
    print('Upper:', U, 'Lower', L)


upperandlowercount()

# Q3h
print('Q3: unique elements of the first list')


def unique():
    N = int(input("Enter list length "))
    A = []
    for i in range(N):
        a = int(input(''))
        A.append(a)
    B = list(set(A))
    print('Unique elements ist:', B)


unique()

# Q4
print('Q4: hyphen-separated sequence after sorting them alphabetically' )
string = input('Enter String :')
A = string.split("-")
A = sorted(A)
print('Alphabetically sorted list', '-'.join(A))

# Q5
print('Q5: characters in the sentence capitalized ')


def upper():
    string = input('Enter String :')
    A = string.upper()
    print('Capitalized string:', A)


upper()

# Q6
print('Q6: two integral numbers in string form and compute their sum and print it in the console.')


def sum2():
    string = input('Enter two numbers:')
    a, b = string.split(" ")
    a = int(a)
    b = int(b)
    print('Sum is', a + b)


sum2()

# Q7
print('Q7: print the string with the maximum length')


def largerstring():
    string1 = input('Enter first string:')
    string2 = input('Enter second string:')
    if len(string1) == len(string2):
        print(string1, '\t', string2)
    elif len(string1) > len(string2):
        print(string1, '\t')
    else:
        print(string2, '\t')


largerstring()

# Q8
print('Q8: print a tuple where the values are square of numbers')


def square():
    A = []
    for i in range(1, 21):
        A.append(i * i)
    B = tuple(A)
    print(B, '\n', type(B))


square()

# Q9
print('Q9: label to identify the even and odd numbers')


def evenorodd(num):
    for i in range(num + 1):
        if i % 2 == 0:
            print(i, ' EVEN')
        else:
            print(i, ' ODD')


evenorodd(int(input('Enter the limit')))

# Q10
print('Q10: filter() to make a list whose elements are even numbers')


def is_even():
    X = list(range(1, 21))
    Y = list(filter(lambda x: x % 2 == 0, X))
    print('Even numbers are:', Y)


is_even()

# Q11
print('Q11: uses map() and filter() to make a list whose elements are squares of even')


def eventhansquare():
    X = list(range(1, 11))
    even = list(filter(lambda x: x % 2 == 0, X))
    Y = list(map(lambda x: x * x, even))
    print('Square of Een numbers are:', Y)


eventhansquare()

# Q12
print('Q12: function to compute 5/0 and use try/except to catch the exceptions')


def except1():
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    try:
        print(num1 / num2)
    except:
        print('Second number cannot be zero')


except1()

# Q13
print('Q13: Flatten the list')
import functools
temp = ''
reduce_number = functools.reduce(lambda x, y: str(x) + temp + str(y), list(range(1, 8)))
print(reduce_number)

# Q14
print('Q14: values which are not divisible by 3 but are a multiple of 7')

l = []
N = int(input("Enter list length "))
for i in range(N):
    a=int(input('Enter List element: '))
    l.append(a)
print(list(filter(lambda x: x % 3 !=0 and x % 7 == 0 , l)))

# Q15
print('Q15: multiply the elements of a list by itself using a traditional function and pass the function to map()')


def list_multiply(list1):
    return list1*list1

l = []
N = int(input("Enter list length "))
for i in range(N):
    a = int(input('Enter List element: '))
    l.append(a)

print(list(map(list_multiply,l)))

# Q16
print('Q16: output of the codes')

print('Ans for 16(a) = 2')
print('Ans for 16(b) = after f\nafter f?\n NameError: name 'f' is not defined')