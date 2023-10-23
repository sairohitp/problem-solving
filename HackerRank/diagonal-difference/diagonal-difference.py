def diagonalDifference(arr):
    leftdiag = rightdiag = 0
    
    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n-1-i]
    
    return abs(leftdiag-rightdiag)

diagonalDifference()