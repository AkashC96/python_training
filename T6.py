# Q1
print('Q1: uppercase using list comprehension ')
input_Str= str(input())
print([x for x in input_Str if x.isupper()])

# Q2
print('Q2: Use Zip function')
alist=['Smit', 'Jaya', 'Rayyan']
blist=['CSE', 'Networking', 'Operating System']
mydict=dict(zip(alist,blist))
print(mydict)

# Q3
print('Q3:')
print('Learned about Yield,next and Generators')

# Q4
print('Q4: using generators to reverse the string.')
inp = 'Consultadd Training'
print(inp)
print(inp[::-1])

# Q5
print('Q5: example on decorators')
def revmethod(txt):
    return txt[::-1]

def lowermethod(txt):
    return txt.upper()

newMethod1= revmethod
newMethod2= lowermethod

txt='Text String for test'
print(newMethod1(txt))
print(newMethod2(txt))