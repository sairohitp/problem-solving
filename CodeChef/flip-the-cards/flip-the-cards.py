t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    # minimum number of flips required to make all cards face-up
    min_flips = min(x, n-x)
    print(min_flips)