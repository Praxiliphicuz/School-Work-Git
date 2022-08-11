#inp = input("type an integer")
#while inp != int(inp)
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 0 :
        break
    try:
        mun = float(num)
    except:
        print('invalid input')
        break

    print(mun)

print("Maximum", largest)
