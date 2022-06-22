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

''' Text '''
x='this is a string'
print(x)

'''
Numeric
'''

''' Integer '''

x=5
print(type(x))
print(x)

''' Float '''

y=5.2
print(type(y))

''' Sequence '''

list_1=[1,2,3]
tuple_1=(1,2,3)
range_1=range(4)

print(type(tuple_1))
print(tuple_1)
print(list(range(6)))

''' Mapping '''

dict_1={'Netherlands':'Amsterdam','USA':'Washington','Japan':'Tokyo'}
print(dict_1.keys())
print(dict_1.values())

''' Boolean '''

print(False)
print(type(False))

'''
1.4 Python operators
'''

'''aritmetic operators'''

print(2+2)
print(2+2.5)
print(3-2)
#print(3*'5')
print(6/3)
print(17%12)
print(2**3)
print(5//2)

'''Comparison operators'''

print(2==2)
print(2==3)
print(2<3)
print(2!=3)

'''Membership operators'''

print('K' in 'ciao')
print('C' in 'Ciao')

'''Identity operators'''

print(4 is 4)
print(4 is 5)
print(4 is not 5)

'''Logical operators'''

x=5
y=6
print(x and y)
print(x or y)

'''
1.5 if/elif/else statement
'''

''' Capitals  '''

list_capitals=['Amsterdam', 'Tokyo', 'Washington']

if 'Amsterdamm' in list_capitals:
    print('Yes')
else:
    print('No')
    
''' Multiples  '''

number=3    

if number % 3 == 0:
    print(str(number) + ' is a multiple of 3.')
else:
    print(str(number) + ' is not a multiple of 3.')

''' Numbers within range '''

number_2=4

if number_2 >= 5 and number_2 <= 10:
    print('Number is within range.')
elif number_2 < 5:
    print('Number is lower than range.')
else:
    print('Number is higher than range.')


'''
1.6 
For Loops
'''

''' Animals '''

list_1=['Cat', 'Dog', 'Bird']

for pet in list_1:
    print('I love my: ' + pet)

''' Capitals for loop '''

capitals={"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

for key, value in capitals.items():
    print('The capital of {key} is {value}.'.format(key=key, value=value) )


''' Ice Cream '''

bottom=['Cone', 'Cup', 'Stick']

base=['Vanilla', 'Chocolate']

top=['Cherry', 'Hagel slag', 'Nuts']

print('All ice cream combinations: ')

for item in bottom:
    for item_2 in base:
        for item_3 in top:
            print('Ice cream bottom: ' + item + ', base: ' + item_2 + ', top: ' + item_3)

'''
While Loops
'''

number=1

while number<5:
    number=number+1
    print(number)



'''
1.7 Functions
'''

''' Shout function '''

def shout_loud(list_here):
    
    for item in list_here:
        if type(item) is str:
            print((item.upper() + '!!!!!!!!'))
        else:
            print('NUMBER!!!!')
      
shout_loud(['dog','cat',1,1.5])


''' Odd even function '''

def odd_even(number):
    if number % 2 == 0:
        return 'The number is even.'
    else:
        return 'The number is odd'


'''
1.8 Classes
'''

''' Class coffee '''
class coffee:

    name='Python Bar'

    def __init__(self, coffee_type):
        self.coffee=30
        self.sip=10
        self.coffee_type=coffee_type

    def take_a_sip(self):
        if self.coffee>0:
            print('I take a sip of my favorite ' + self.coffee_type)
            self.coffee=self.coffee-self.sip
            return self.coffee
            
        elif self.coffee==0:
            return 'out of ' + self.coffee_type + '!!!!!!'


    


a=coffee('espresso')
print(coffee.name)
print(a.take_a_sip())
print(a.take_a_sip())
print(a.take_a_sip())
print(a.take_a_sip())

'''
Various
'''

dir()
print(print.__doc__)


import pandas
dir(pandas)
pandas.__doc__
pandas.DataFrame.__doc__

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pandas.DataFrame(d)

