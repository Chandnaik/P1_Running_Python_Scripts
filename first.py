
# Arithmetic operation
a = 56
b = 23
add = a + b
sub = a - b
multiply = a * b
division =  a/b

print('Sum of {} and {} is {}'.format(a,b,add))
print('Diffrence between {} and {} is {}'.format(a,b,sub))
print('Product of {} and {} is {}'.format(a,b,multiply))
print('Division of {} and {} is {}'.format(a,b,division))



print(type(a))
print(type(str(a)))
print(type(float(a)))
print((bool(a)))
print(a)
print(type(a))






# if else loop
if a > b:
    print('{} is greater'.format(a))
elif a == b:
    print('{} is equal to {}'.format(a,b))
else:
    print('{} is smaller'.format(a))
print("out from if else condition")





#list
flower = ["rose","lotus","champa","mogra"]
for f in flower:
    print(f)
print("the flowers name as been printed")


#numbers
number = [20,476,34,872,67]
print("number in list")
for n in number:
    print(n)
print("number greater than 50 are")
for x in number:
    if x > 50:
        print(x)


