def find_least_integer(A, B, C, K):
    left, right = 0, K
    result = -1

    while left <= right:
        mid = (left + right) // 2
        equation_result = A * mid * mid + B * mid + C

        if equation_result >= K:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    A, B, C, K = map(int, input().split())
    result = find_least_integer(A, B, C, K)
    print(result)