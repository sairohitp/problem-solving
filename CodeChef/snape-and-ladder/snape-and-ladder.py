import math

t = int(input())

for i in range(t):
    b, ls = map(int, input().split())
    
    min_rs = math.sqrt(ls**2 - b**2)
    max_rs = math.sqrt(ls**2 + b**2)
    
    print("{:.5f} {:.5f}".format(min_rs, max_rs))
