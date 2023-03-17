for i in range(int(input())):
    x,y,z=map(int,input().split())
    m=min(y,z);
    y-=m;
    z-=m;
    if(x>y and x>z):
        print("YES")
    else:
            print("NO")