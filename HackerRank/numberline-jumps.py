"""

Jumps can be calculated via following
x1 += v1
x2 += v2

"""

def kangaroo(x1, v1, x2, v2):
    if (v1 < v2):
      return "NO"

    if ((x2 - x1) % (v1 - v2) == 0):
      return "YES"
    else:
      return "NO"


"""

Code method 2:

"""
x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

exist = False

while(True): #jumping is continuing
    if x1 == x2:
        exist = True
        break
    if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1) or (v2 == v1 and x2 != x1): #testcases where the jumping matches, more velocity, etc.
        break

    # update jump location
    x1 += v1
    x2 += v2
    
if exist:
    print('YES')
else:
    print('NO')