import string
char2=string.ascii_uppercase

char="<1T <5Y <2C <5W >7H >3C >13J >4A"

mo=""
char=char.split()
for i in range(len(char)):
    if char[i][0]== '<':
        print(char2[char2.index(char[i][2]) - int(char[i][1])])
    else:
        print(char2[char2.index(char[i][2]) + int(char[i][1])])



#print(char2.index("T"))

