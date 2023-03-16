def min_elements_to_remove(n, arr):
    negative_count = 0
    zero_count = 0
    for num in arr:
        if num < 0:
            negative_count += 1
        elif num == 0:
            zero_count += 1
    if negative_count % 2 == 0:
        return 0
    elif zero_count > 0:
        return 0
    else:
        return 1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_elements_to_remove(n, arr))
