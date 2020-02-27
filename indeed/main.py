s = input()

a = {}
m = {}
acc = 0
for c in s:
    for k in a.keys():
        a[k] += m[k]
    if c not in a.keys():
        a[c] = 1
    m[c] = m[c]+1 if c in m else 1

for k in a.keys():
    a[k] += m[k]

print(a, m)
out = sorted(a.keys(), key=lambda x: a[x]*-1)
for o in range(len(out)):
    if o > 0:
        if a[out[o-1]] == a[out[o]] and out[o-1] > out[o]:
            out[o-1], out[o] = out[o], out[o-1]
sss = ""
for o in out:
    sss += o
print(sss)
