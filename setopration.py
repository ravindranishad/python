A = {1,2,3,4,5}
B = {4,5,6,7,8,}
# use union functionn
print(A | B)
print(A & B)
print(A - B)
print(B - A)


x = {2,3,4,7}
y = {2,3,4,7,6,5,8}
print(x.issubset(y))
z = {3,5,8,10,11}
print(x.issubset(z))
a = {11,12,13}
print(a.isdisjoint(y))

x = [2,2,3,5,5,6,6]
xs = set(x)
xl = list(set(x))
print(x)
print(xs)
print(xl)