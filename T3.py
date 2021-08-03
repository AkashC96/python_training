#Q1
print('Q1')
x=[1,2,3,4.01,12.4,34.6,1+1j,12+2j,'Hello','World']
print(x)


#Q2
print('Q2')
list1=[1,2,3,4,5]
print(list1[:5])
print(list1[1:5:3])
print(list1[:5:2])

#Q3
print('Q3')
l = []
N = int(input("Enter list length "))
mul=1
sum=0
for i in range(N):
    a=int(input('Enter List element: '))
    l.append(a)
    sum=sum+a
    mul=mul*a
print("the sum of the list is: ", sum)
print("the product of the list is: ", mul)

#Q4
print('Q4')
l = []
N = int(input("Enter list length "))
mul=1
sum=0
for i in range(N):
    a=int(input('Enter List element: '))
    l.append(a)
print("the minimum of the list is: ", min(l))
print("the maximum of the list is: ", max(l))

#Q5
print('Q5')
l = []
N = int(input("Enter list length "))
mul=1
sum=0
for i in range(N):
    a=int(input('Enter List element: '))
    l.append(a)
    l = [x for x in l if x % 2 == 1]
print(l)

#Q6
print('Q6')

squared_list = []
for i in range(1,31):
    if i < 6 or i > 25:
        a = i * i
        squared_list.append(a)
print(squared_list)

#Q7
print('Q7')
l1 = []
N = int(input("Enter 1st list length "))
for i in range(N):
    a=int(input('Enter 1st List element: '))
    l1.append(a)

l2 = []
N = int(input("Enter 2nd list length:"))
for i in range(N):
    a=int(input('Enter 2nd List element: '))
    l2.append(a)
print(l1,l2)
l3=l1
l3.extend(l2)
print(l3)

#Q8
print('Q8')
x=int(input('Enter length of dictionary 1 : '))
y=int(input('Enter length of dictionary 2 : '))
dict1 = {}
for d in range(1,x):
    dict1[d]=int(input('Enter dictionary 1 element'))
for d in range(1,y):
    dict2[d]=int(input('Enter dictionary 2 element'))

print(dict1,dict2)
dict3=dict1
dict3.update(dict2)
print(dict3)


#Q9
print('Q9')
x=int(input('Enter x: '))
dict = {}
for d in range(1,x+1):
    dict[d]=d*d
print(dict)


#Q10

print('Q10')
x=input('Enter elements with commas in b/w : ')
print(x)
l=[]
a=0
for i in x:
    if i != ',':
        a = 10 * a + int(i)
    if i == ',':
        l.append(str(a))
        a=0
l.append(str(a))
t=tuple(l)
print('List: ',l,'\nTuple :',t)