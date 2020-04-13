from basic_methods import *
class Calculator:

    a=int(input('Enter first number'))
    cal=str(input('Enter sign.'))
    b = int(input('Enter second number.'))
    if cal=='+':
        res=add(a,b)
        print('Sum is =',res)
    elif cal=='-':
        res=subt(a,b)
        print('Subtraction is=',res)
    elif cal=='*':
        res=mult(a,b)
        print('Multiplication is=',res)
    elif cal=='/':
        res=divi(a,b)
        print('Division is=',res)
    elif cal=='%':
        res=mod(a,b)
        print('Module is=',res)
    elif cal=='//':
        res=rem(a,b)
        print('Remainder is=',res)
    else:
        print('Not Designed.')