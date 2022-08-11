
def computepay(hours, rate):

    base_rate = rate
    overtime_rate = rate*1.5

    overtime_hours = hours - 40 if hours > 40 else 0
    base_hours = 40 if hours > 40 else hours

    base_pay = base_hours*base_rate
    overtime_pay = overtime_hours*overtime_rate

    return(base_pay+overtime_pay)


hours = input("what is hours")
rate = input("What is Rate")

print("Your total pay is:")
print(computepay(float(hours), float(rate)))




#assert computepay(23.0, 70.0) == 1610
#assert computepay(45.0, 10.50) == 498.75
#assert computepay(0.0, 5.00) == 0.0
