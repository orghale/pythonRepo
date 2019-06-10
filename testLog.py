import logging

logging.basicConfig(filename = 'test.log', level=logging.DEBUG, format = '%(asctime)s : %(created)f:%(levelname)s:%(message)s')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x * y

def div(x,y):
    return x/y

a=10
b=2

addition = add(a,b)
print('add: {} + {} = {}'.format(a,b,addition))
logging.debug('add: {} + {} = {}'.format(a,b,addition))

subtraction = sub(a,b)
print('Subtract: {} - {} = {}'.format(a,b,subtraction))
logging.debug('subtract: {} - {} = {}'.format(a,b,subtraction))

multiply = mul(a,b)
print ('Multiply: {} * {} = {}'.format(a,b,multiply))
logging.debug('Multiplication: {} * {} = {}'.format(a,b,multiply))

divide = div(a,b)
print('Division: {} / {} = {}'.format(a,b,divide))
logging.debug('division: {} / {} = {}'.format(a,b,divide))

