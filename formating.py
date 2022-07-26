from itertools import product


product= input("what item did you buy? ")
price = float(input("how much did you pay"))
qty = int(input("how many did you buy?"))

print('you purchased',qty,product,'for',price)

#formated string
print(f'YOU purchase {qty} {product} for {price}')