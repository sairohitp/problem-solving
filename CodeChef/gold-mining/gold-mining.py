t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    if (n+1)*y >= x:
        print("YES")
    else:
        print("NO")
