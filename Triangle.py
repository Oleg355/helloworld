import math
a = int(input('Side 1'))
b = int(input('Side 2'))
c = int(input('Side 3'))
p = (a+b+c)/2
print("Triangle S ",math.sqrt(p*(p-a)*(p-b)*(p-c)))
