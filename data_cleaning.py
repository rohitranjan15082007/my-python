str = input ("Enter the sentence or string :")
clean = ''
for x in str :
    if x.isalpha() or x.isspace():
        clean = clean + x
    else:
        clean = clean + ' '
print(clean)