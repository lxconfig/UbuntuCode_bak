
import math

while True:
    n = int(input())
    a = 1
    for i in range(1, n+1):
        a = a*i
    print(int(a % (math.pow(10, 6) + 3)))