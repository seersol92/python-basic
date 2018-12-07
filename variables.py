x = 1 #init
y = 2.5 #float
name = 'hadi' #str
is_cool = True #Bool Cap True or Cap False

# multiple assignmet
x,y,name,is_cool = (1, 2.5, 'hadi', True)

print(x,y,name,is_cool)

#check variable type
print(type(x))


#Casting datatypes

x = str(x)
y = int(y)

print(type(y), y, type(x))