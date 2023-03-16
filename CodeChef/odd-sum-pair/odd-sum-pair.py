def is_odd_sum(a, b):
    return (a + b) % 2 == 1

def solve():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())

        # check if there are two numbers with an odd sum
        if is_odd_sum(a, b) or is_odd_sum(b, c) or is_odd_sum(c, a):
            print("YES")
        else:
            print("NO")

solve()