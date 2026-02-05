a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
    print(f"{a} is maximum")
elif b>c:
    print(f"{b} is maximum")
else:
    print(f"{c} is maximum")
if a<b and a<c:
    print(f"{a} is minimum")
elif b<c:
    print(f"{b} is minimum")
else:
    print(f"{c} is minimum")
