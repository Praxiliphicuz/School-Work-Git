#this is a check on 3.1's homework and your putting xyzin front of pay in the print statment to see if both come up with the same output in the end
hrs = input("Enter Hours")
rte = input('hourly rate')
try:
    x = float(hrs)
    y = float(rte)
except:
    print('error,please enter numeric input')

print(x, y)
if (x) > 40 :
    z = y * x
    w = (x - 40.0) * (y * .5)
    xp = z + w
else:
    xp = x * y
print("Pay:",xp)
