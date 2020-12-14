

n = int(input())
a = 1
for i in range(1, n+1):
    a = a*i
for j in str(a)[::-1]:
    if j != "0":
        print(int(j))
        break
        
