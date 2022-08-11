largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        num = int(num)
    except:
        print('invalid input')
        continue
    if largest is None :
        largest = num
    elif largest < num :
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
print ("Maximum is", largest)
print ("Minimum is", smallest)
#continue the loops and go back to asking input

#if the loop reaches this point, we knonw its a positve number, so just add continue
