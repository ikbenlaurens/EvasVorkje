'''
1.1 Printing a string
'''
print('hello world')

'''
1.2 Python variables
'''
x=5
x=7
z='hello'
y=12

print(x)


'''
1.3 Datatypes
'''

'''
Text
'''
x='this is a string'
print(x)

'''
Numeric
'''
print('Integer: ')
x=5
print(type(x))
print(x)
print('--------------')
print('Float: ')
y=5.2
print(type(y))
print('--------------')
print('Sequence')
list_1=[1,2,3]
tuple_1=(1,2,3)
range_1=range(4)
print(type(tuple_1))
print(tuple_1)
print('--------------')
print('Mapping')
dict_1={'Netherlands':'Amsterdam','USA':'Washington','Japan':'Tokyo'}
print(dict_1.keys())
print(dict_1.values())
print('--------------')
print('Boolean: ')
print(False)
print(type(False))



'''
1.4 Python operators
'''
print('Aritmetic operators')
print(2+2)
print(2+2.5)
print(3-2)
#print(3*'5')
print(6/3)
print(17%12)
print(2**3)
print(5//2)
print('Comparison operators')
print(2==2)
print(2==3)
print(2<3)
print(2!=3)
print('Membership operators')
print('K' in 'ciao')
print('C' in 'Ciao')
print('Identity operators')
print(4 is 4)
print(4 is 5)
print(4 is not 5)
print('Logical operators')
x=5
y=6
print(x and y)
print(x or y)



'''
1.5 if else statement
'''
dict_capitals={'Netherlands':'Amsterdam','USA':'Washington','Japan':'Tokyo'}
list_capitals=list(dict_capitals.values())

if 'Amsterdamm' in list_capitals:
    print('Yes -nl')
elif 'Washington' in list_capitals:
    print('Yes -usa')
else:
    print('No')



print('some more code')


'''
1.6 
For Loops
'''
name='Giuseppe'
number=556
list_1=['Dog', 'Cat', 'Bird']
dictionary={"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

for item in dictionary.values():
    print(item)

'''
While Loops
'''
answers='Haarlem'

capitals={'Noord Holland':'Haarlem'}

number=1

while number<5:
    number=number+1
    print(number)



'''
1.7 Functions
'''

def shout_loud(list_here):
    
    for item in list_here:
        if type(item) is str:
            print(item.upper() + '!!!!!!!!')
        else:
            print('NUMBER!!!!')
      
shout_loud(['dog','cat',1,1.5])



'''
1.8 Classes
'''


print(type(5))

print(dir(5))


class coffee:
    def __init__(self):
        self.coffee=30
        self.sip=10

    def take_a_sip(self):
        if self.coffee>0:
            print(self.coffee)
            self.coffee=self.coffee-self.sip
            
        elif self.coffee==0:
            print('out of coffee!!!')

class coffee_1:
    def __init__(self):
        self.coffee=30
        self.sip=10

    def take_a_sip(self):
        if self.coffee>0:
            print(self.coffee)
            self.coffee=self.coffee-self.sip
            
        elif self.coffee==0:
            print('out of coffee!!!')
    


a=coffee()
print(a.take_a_sip())
print(a.take_a_sip())
print(a.take_a_sip())
print(a.take_a_sip())


b=coffee()
print(b.take_a_sip())
print(b.take_a_sip())
print(b.take_a_sip())
print(b.take_a_sip())


print(print.__doc__)


import pandas

print(len(dir(pandas)))
