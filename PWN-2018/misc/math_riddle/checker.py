from decimal import *

# Set precision to 1000 decimal places
getcontext().prec=1000


a = Decimal(int(input("Eggplant:")))

b = Decimal(int(input("Banana:")))

c = Decimal(int(input("Peach:")))

assert a > 0
assert b > 0
assert c > 0
assert len(str(a)) < 200
assert len(str(b)) < 200
assert len(str(c)) < 200
assert 10 == a/(b+c) + b/(a+c) + c/(a+b)

with open("/opt/flag.txt") as f:
    print(f.read())

