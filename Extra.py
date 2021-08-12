# Q1
print('Q1: Access list')
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[-3:])
print(x[::2])
print(x[::-1])
print([x[5][5][0]])
print(list())

# Q2
print('Q2: range vs xrange')
print(list(range(1001)))
print(list(range(1001)))
print('Type(range)=list,Type(xrange)=xrange')

# Q3
print('Q3:Tulips are immutable ,faster as compared to list')

# Q4
print('Q4:print the number which is divisible by 3 and is a multiple of 2.')
ans =[]
for i in range(1,101):
    if(i%3==0) and (i%2==0):
        ans.append(str(i))
print(ans)

# Q5
print('Q5: string with their index')
string='abcdefghijklmnopqrstuvwxyz'
string = string[::-1]
print(string)
for i, vowel in enumerate(string):
    if vowel.lower() in 'aeiou':
        print(i,vowel)

# Q6
print('Q6:print the string which is having an even length')
string = "hello my name is abcede"
string= string.split(" ")
for i in string:
    if len(i) % 2 == 0:
        print(f"string: {i}\tlenght of string is: {len(i)}")

# Q7
print('Q7: sum is equal to the result number 8')
x=[1,2,3,4,5,6,7,8,9,-1]
s = []
sum =8
for i in x:
    temp = sum - i
    if temp in s:
        print(i, temp)
    s.append(i)

# Q8
print('Q8: Python to complete the task ')
even = []
sume=0
odd = []
sumo=0
maxe=0
maxo=0
while len(even) < 5 or len(odd) < 5:
    a = int(input("enter a number in the range 1 and 50: "))
    if a % 2 == 0:
        if len(even) < 5:
            even.append(int(a))
            sume=sume+a
            if a>maxe:
                maxe=a
        else:
            pass
    else:
        if len(odd) < 5:
            odd.append(int(a))
            sumo=sumo+a
            if a>maxo:
                maxo=a
        else:
            pass
else:
    pass
print('even list',even,'Sum',sume,'Max',maxe)
print('odd list',odd,'Sum',sumo,'Max',maxo)

# Q9
print('Q9:occurrence of a specific character from an alphanumeric string.')

string = str(input("enter your input string: "))
countalpha = {}
for i in string:
    if i in "abcdefghijklmnopqrstuvwxyz":
        countalpha[i] = string.count(i)

for a, b in countalpha.items():
    print(str(a)+"="+str(b))

# Q10
print('Q10:even numbers in the given tuple ')

def even(num):
    return tuple(filter(lambda x: x % 2 == 0,num))


print(tuple(range(1,11)))
print(even(range(1,11)))