F = [0,1]

x = int(input())
for n in range(2,x+1):
  Fn = F[ n-1 ] + F[ n-2 ]
  F.append(Fn)

print(F[x])