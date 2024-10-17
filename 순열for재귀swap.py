# 조합 for 구현
# 6C4
def itercomb(n) :
    cnt = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    print(i,j,k,l)
                    cnt+=1
    print(cnt)
    

a = []

def curcomb(n, a, b) :
    
    if(b==0) :
        print(a)
        return 1
    
    c = 0
    ret = 0
    if len(a) == 0:
        c = 0
    else :
        c = a[-1]
    for i in range(c+1, n) :
        a.append(i)
        ret += curcomb(n, a, b-1)
        a.pop()
    return ret
    
                    
itercomb(7)
print(curcomb(7, a, 4))



n = int(input())

a = []

def rec(n, a, b) :
    if (n==b) :
        for i in a :
            print(i, end = ' ')
        print()
    for i in range(1, n+1) :
        if i not in a:
            a.append(i)
            rec(n, a, b+1)
            a.pop()
     
rec(n, a, 0)
