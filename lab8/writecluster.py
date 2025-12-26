from random import randint
d1minx = 5
d1maxx = 15
d1miny = 5
d1maxy = 20
d2minx = 5
d2maxx = 15
d2miny = 16
d2maxy = 50
"""
d3minx = 30
d3maxx = 50
d3miny = 15
d3maxy = 30
"""
"""
d4minx = 5
d4maxx = 10
d4miny = 15
d4maxy = 20
"""
kmin = min(d1minx, d1maxx, d1miny, d2maxy, d2minx, d2maxx, d2miny, d2maxy)
kmax = max(d1minx, d1maxx, d1miny, d2maxy, d2minx, d2maxx, d2miny, d2maxy)
n1 = 1000
n2 = 1000
n3 = 100
n4 = 100
x1 = []
x2 = []
y = []
for i in range(n1):
    x1.append(randint(d1minx, d1maxx) / kmax)
    x2.append(randint(d1miny, d1maxy) / kmax)
    y.append(1 / kmax)
for i in range(n2):
    x1.append(randint(d2minx, d2maxx) / kmax)
    x2.append(randint(d2miny, d2maxy) / kmax)
    y.append(20 / kmax)
"""
for i in range(n3):
    x1.append(randint(d3minx, d3maxx) / kmax)
    x2.append(randint(d3miny, d3maxy) / kmax)
    y.append(10 / kmax)
"""
"""
for i in range(n4):
    x1.append(randint(d4minx, d4maxx) / kmax)
    x2.append(randint(d4miny, d4maxy) / kmax)
    y.append(4 / kmax)
"""
"""
counter = 0
for i in range(1000000):
    x1i = randint(kmin, kmax)
    x2i = randint(kmin, kmax)
    if not ((d1minx < x1i < d1maxx and d1miny < x2i < d1maxy) or (d2minx < x1i < d2maxx and d2miny < x2i < d2maxy) or (d3minx < x1i < d3maxx and d3miny < x2i < d3maxy)):
        x1.append(x1i / kmax)
        x2.append(x2i / kmax)
        y.append(4 / kmax)
        counter += 1
        if counter == 2000:
            break
"""
length = len(x1)
index = length - 1
with open('clasters.txt', 'w', encoding='utf-8') as f:
    f.write(str(x1[0]))
    f.write(' ')
    f.write(str(x2[0]))
    f.write(' ')
    f.write(str(y[0]))
    f.write('\n')
    f.write(str(x1[n1 + 1]))
    f.write(' ')
    f.write(str(x2[n1 + 1]))
    f.write(' ')
    f.write(str(y[n1 + 1]))
    f.write('\n')
    """
    f.write(str(x1[n1 + n2 + 2]))
    f.write(' ')
    f.write(str(x2[n1 + n2 + 2]))
    f.write(' ')
    f.write(str(y[n1 + n2 + 2]))
    f.write('\n')
    """
    for i in range(length):
        f.write(str(x1[i]))
        f.write(' ')
        f.write(str(x2[i]))
        f.write(' ')
        f.write(str(y[i]))
        if i != index:
            f.write('\n')
print('Запись завершена.')
