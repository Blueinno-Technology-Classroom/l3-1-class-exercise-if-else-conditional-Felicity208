##################################################
'''
Q1:
a:  True
b:  False
c:  True
d:  False
e:  True
f:  False
g:  True   (corrected)
h:  True
i:  True   (corrected)
'''

##################################################
'''
Q2:
a:  y > 0
b:  z != 0
c:  y > z
d:  z >= 0
e:  abs(y - x) < abs(y - z)    (corrected)
f:  z % 2 != 0
g:  x % 2 == 0
h:  y % z == 0
i:  y >= 0 and y < 10    (corrected)       
j:  x == -z
k:  (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0) | x * y % 2 == 0 and (x + y) % 2 != 0   (corrected)
'''

##################################################
'''
Q3:
'''

number = int(input('Give me a number: '))

if number % 2 == 0:
    if number % 3 == 0:      
        print("Divisible by 6.")
else:
    print("Odd number.")

##################################################
