text = "X-DSPAM-Confidence:    0.8475";
ftext = text.find('.')
#ntext = float(ftext)
print(text[ftext-1:ftext+4]
