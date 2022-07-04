import random

r = 1000
count = 0

for i in range(r**2):
    x = random.randint(0,r)
    y = random.randint(0,r)
    if (x**2+y**2<=r**2):
        count+=1
print(count*4/r**2)
