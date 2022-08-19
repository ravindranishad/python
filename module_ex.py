from random import random
from random import radint, choice, shuffle, choices

val = random()
print(val)

for i in range(10):
    val = radint(1, 10)
    print(val, end='')

nums = []
for i in range(10):
    nums.append(radint(1, 1000))
print("\n",nums)

animals = ['🦎','🐊','🐍','🐉','🐢','🦖','🐬']

sel_ani= choices(animals)
print(f'selcted animal: {sel_ani}')

sel_ani =choices(animals, k=3)
print(f'shuffle animals: {"".join(animals)}')