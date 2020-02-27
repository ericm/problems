t = int(input())
abxy = []
for _ in range(t):
    abxy.append(tuple((int(x) for x in input().split())))

for ab in abxy:
    ded = (ab[2], ab[3])
    res = (ab[0], ab[1])
    x = (res[0]-ded[0], ded[0])
    y = (res[1]-ded[1], ded[1])
    print(max(x[0]*(y[0]-1), (x[0]-1)*y[0], x[1]*(y[1]-1),
              (x[1]-1)*y[1], (x[0]-1)*res[1], res[0]*(y[1]-1),
              (x[1]-1)*res[1], res[0]*(y[0]-1),
              (res[0])*(y[1]),
              (res[1])*(x[1]),
              ))
