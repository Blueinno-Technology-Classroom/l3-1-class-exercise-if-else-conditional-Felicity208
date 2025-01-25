##################################################
'''
Q1:
a:  True
b:  False
c:  True
d:  False
e:  True
f:  False
g:  False
h:  True
i:  False
'''

##################################################
'''
Q2:
a:  y > 0
b:  z != 0
c:  y > z
d:  z >= 0
e:  x - y > z - y
f:  z % 2 != 0
g:  x % 2 == 0
h:  y % z == 0
i:  y > 9
j:  0 - x != 0 - z
k:  (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0)
'''

##################################################
'''
Q3:
'''

number = int(input('Give me a number: '))

if number % 2 == 0:
    if number % 3 == 0 and number % 2 == 0:
        print("Divisible by 6.")
else:
    print("Odd number.")

##################################################
