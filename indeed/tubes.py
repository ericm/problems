n = int(input())
i1 = set()
i2 = set()
i3 = set()
i4 = set()
for _ in range(n):
    ip = input().split(".")
    i1.add(ip[0])
    i2.add(ip[1])
    i3.add(ip[2])
    i4.add(ip[3])
ip = ""
ss = 0
if len(i1) == 1:
    for i in i1:
        ip += str(i)+"."
    ss += 8
else:
    t = 0
    for i in i1:
        t &= int(i)
    ip += str(t)+"."

if len(i2) == 1:
    for i in i2:
        ip += str(i)+"."
    ss += 8
else:
    t = 0
    for i in i2:
        t &= int(i)
    ip += str(t)+"."
if len(i3) == 1:
    for i in i3:
        ip += str(i)+"."
    ss += 8
else:
    t = 0
    for i in i3:
        t &= int(i)
    ip += str(t)+"."
if len(i4) == 1:
    for i in i4:
        ip += str(i)
    ss += 8
else:
    t = 0
    for i in i4:
        t &= int(i)
    ip += str(t)

print(ip+"/"+str(ss))
