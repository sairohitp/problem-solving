def beautifulDays(i, j, k):
    beautday = 0

    for day in range(i, j+1):
        rev = int(str(day)[::-1])
        if (abs(rev-day)%k==0):
            beautday+=1

    return beautday