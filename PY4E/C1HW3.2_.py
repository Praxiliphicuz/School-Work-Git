#this is a check on 3.1's homework and your putting xyzin front of pay in the print statment to see if both come up with the same output in the end
hrs = input("Enter Hours")
rte = input('hourly rate')
x = float(hrs)
y = float(rte)
if (x) > 40 :
    z = y * x
    w = (x - 40.0) * (y * .5)
    xp = z + w
else:
    xp = x * y
print("xyz Pay:",xp)
