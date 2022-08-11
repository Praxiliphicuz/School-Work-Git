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
print("Pay:",xp)
