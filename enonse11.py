# pi piti ak pi gwo eleman nan lis

lismwen = [10, 20, 4, 45, 99,55,48,16]
#pi piti valè a

def min(lismwen):
    minimum = lismwen[0]
    for x in lismwen:
        if x < minimum :
            minimum = x
    return minimum

#pi gwo valè a
def max(lismwen):
    maximum = lismwen[0]
    for x in lismwen:
        if x > maximum :
            maximum = x
    return maximum

print("\nlis mwen an se:",lismwen,"\n")
print("pi piti eleman an se:", min(lismwen))
print("pi gwo eleman an se:", max(lismwen))
