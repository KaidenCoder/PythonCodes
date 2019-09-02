decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)

for i in range(3,40,3):
    print(i)

print(my_range == range(3, 40, 3))  


o = range(0, 100, 4)
print(o)
p = o[0::5]
print(p)
for i in p:
    print(i)
