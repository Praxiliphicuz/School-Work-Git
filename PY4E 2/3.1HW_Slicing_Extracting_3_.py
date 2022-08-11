text = 'X-DSPAM-Confidence:    0.8475'
ftext = text.find('0')
print(ftext)
ntext = text.find('5',ftext)
print(ntext)
htext = text[ftext+1:ntext+1]
print(htext)
fltext = float(htext)
print(fltext)
#htext = (text[ftext+5])
