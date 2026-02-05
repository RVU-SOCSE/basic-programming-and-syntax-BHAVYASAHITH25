op=input("enter operator(+,-,*,/,%,//):")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
match op:
    case '+':
        print("result=",a+b)
    case '-':
        print("result=",a-b)
    case '*':
        print("result=",a*b)
    case '/':
        print("result=",a/b)
    case '%':
        print("result=",a%b)
    case '//':
        print("result=",a//b)
    case _:
        print("invalid answer")
