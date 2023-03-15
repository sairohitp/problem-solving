t = int(input())

for i in range(t):
    l, r = map(int, input().split())
    count = 0 

    for j in range(l, r+1):
        last_digit = j % 10  # last digit of the number

        if last_digit == 2 or last_digit == 3 or last_digit == 9:
            count += 1

    print(count)
