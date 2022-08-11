# get the name of ht e file and open it
name = input('Enter file:')
handle = open(name, 'r')

# count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts [word] = counts.get(word,0) + 1

        # find the most common word
        bigcount = none
        bigword = none
        for word, count in counts.items():
            if bifcount is none or count >bigcount:
                bigword = word
                bigcount = count

                # all done
                print(bigword,bigcount)
