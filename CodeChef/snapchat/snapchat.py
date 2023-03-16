def max_streak_count(n, chef_snaps, chefina_snaps):
    streak_count = 0
    max_streak_count = 0
    for i in range(n):
        if chef_snaps[i] > 0 and chefina_snaps[i] > 0:
            streak_count += 1
        else:
            streak_count = 0
        max_streak_count = max(max_streak_count, streak_count)
    return max_streak_count

def main():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # number of days observed
        chef_snaps = list(map(int, input().split()))  # chef's snaps
        chefina_snaps = list(map(int, input().split()))  # chefina's snaps
        max_count = max_streak_count(n, chef_snaps, chefina_snaps)  # find the maximum streak count
        print(max_count)

if __name__ == '__main__':
    main()
