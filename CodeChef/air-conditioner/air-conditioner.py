# function to check if a temperature fits all demands
def is_possible(a, b, c, temp):
    return (temp >= a) and (temp <= b) and (temp >= c)

t = int(input().strip())
for _ in range(t):
    a, b, c = map(int, input().split())
    min_temp = max(a, c)
    max_temp = min(b, c)
    if min_temp <= max_temp:
        print("Yes")
    else:
        print("No")
