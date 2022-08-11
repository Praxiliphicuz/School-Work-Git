largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 0 :
        break
    try:
        mun = int(num)
    except:
        print('invalid input')
        break

    print(mun)

print("Maximum is", largest)
print("minimum is", smallest)
