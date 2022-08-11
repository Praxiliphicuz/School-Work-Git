score = input('enter score')
try:
    x = float(score)
except:('print error numeric iput')
try:
    x >= 0.9
    print("a")
    x >= 0.8
    print("b")
    x >= 0.7
    print("c")
    x >= 0.6
    print("d")
    x >= 0.5
    print("f")
except:
    if x > 1.0 :
        print('Error Over Score limit')
    else:
        x < 0.5
    print('Error score under range')
(quit)
