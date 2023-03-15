def can_make_equal(A, B):
    if abs(A - B) % 2 == 0:
        return "YES"
    else:
        return "NO"

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(can_make_equal(A, B))
