t = int(input())
while t:
    a, b, c, = list(map(int, input().split()))
    if a != b and b != c and a != c:
        print("YES")
    else:
        print("NO")
    t -= 1
