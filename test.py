n = int(input())

for i in range(1, n+1) :
  if i%10==3 :
    print("X", end=' ') 
  else:
    print(i, end= ' ')