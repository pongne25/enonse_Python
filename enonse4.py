#milptip a ak miltip b

a = 2
b = 3
c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d=[]
e=[]
f=[]
g=[]
for i in c:

    if i%a==0 and i%b!=0:
        d.append(i)


    if i%b==0 and i%a!=0:
        e.append(i)


    if i%a==0 and i%b==0:
        f.append(i)


    if i%b!=0 and i%a!=0:
        g.append(i)


print(d,"--> Total nonb: ",len(d))
print(e, "--> Total nonb: ",len(e))
print(f, "--> Total nonb: ",len(f))
print(g, "--> Total nonb: ",len(g))