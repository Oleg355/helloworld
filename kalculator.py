
def plus(x,y):
    r = x+y
    print(r)
    return r
    
def minus(x,y):
    r = x-y
    print(r)
    return r
    
def umn(x,y):
    r = x*y
    print(r)
    return r
    
def dele(x,y):
    r = x/y
    print(r)
    return r

print("Это калькулятор. Что нужно знать еще?")
while True:
    x = int(input("1 число: "))
    y = int(input("2 число: "))
    c = input("Операция: ")
    
    if c == '+':
        plus(x,y)
    elif c == '-':
        minus(x,y)
    elif c == '*':
        umn(x,y)
    elif c == '/':
        dele(x,y)
