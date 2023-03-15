# n = number of friends
# x = number of slices
def minimum_pizzas(n, x):
    total_slices = n * x
    pizzas = (total_slices + 3) // 4
    return pizzas

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    pizzas = minimum_pizzas(n, x)
    print(pizzas)
