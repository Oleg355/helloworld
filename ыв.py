a = int(input())
b = int(input())
c = int(input())
if a>b+c:
    raise Exception('Not exist')
elif a+b<c:
    raise Exception('Not exist')
elif a+c<b:
    raise Exception('Not exist')
else:
    print('Exist')
