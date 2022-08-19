from zoneinfo import InvalidTZPathWarning


x = [7,5,3,12]
x2 = []
for i in x:
    s = i ** 2
    x2.append(s)

print(x) 
print(x2)   


x = [2,3,5,4]
y = [3,6,5,3]
z = []
for i,j in zip (x,y):
    z.append(i+j)
    print(z)

    x = [2,5,8,7,3,6,10]
    x2 = [i ** 2 for i in x ]
    print(x2)

    x = [12,5,64,5,34,2,3]
    x2 = [i ** 2 for i in x]
    print(x)
    print(x2)
    y = [2,3,5,6,7,7,2]

    z = [i + j for i ,j in zip(x,y)]
    print(z)

name = ['Brace Wayne','clork kent','Wally West']
initial = [] 

for name in name :
    parts = name.split()
    initial.append(parts[0][0]+parts[-1][0])
    print(initial)