def plusMinus(arr):
    pov = neg = zero = 0
    
    for i in range(n):
        if arr[i] > 0:
            pov+=1
        elif arr[i] < 0:
            neg+=1
        else:
            zero+=1
    
    print(pov/n)
    print(neg/n)
    print(zero/n)

plusMinus()