t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    original_days = [((i-1)//5)+1 for i in range(1, n+1)]
    k_day = original_days[k-1]
    original_days.pop(k-1)
    shifted_days = [((i-1)//5)+1 for i in range(1, n)]
    num_changed = sum([1 for i in range(n-1) if original_days[i]!=shifted_days[i]])
    print(num_changed)
