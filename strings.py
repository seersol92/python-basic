 # Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Hadi'
age = 24

# Concatenate
#print('Hello, my name is'+ name +'  and I am ' + age) #""" will be error as print age is int """

print('Hello, my name is'+ name +'  and I am ' + str(age)) #By casting age as String



# /*** String Formatting ****/

# 1 Arguments by Position 

print('Hello, my name is {name} and i\'m {age}.'.format(name=name, age=age) )


# 2 F Strings PY(3.6+)
print(f'Hello, my name is {name} and i\'m {age}.' )


# String Methods