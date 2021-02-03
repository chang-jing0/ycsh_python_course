F = [0,1]
b = []

x = int(input())
y = int(input())
z = x
for n in range(2,y+1):
  Fn = F[ n-1 ] + F[ n-2 ]
  F.append(Fn)
while x<=y:
  a = F.pop(z)
  b.append(a)
  x += 1
print(b)
