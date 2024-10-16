n = int(input())

m = [0 for i in range(1000001)]
m[0]=0
m[1]=1
m[2]=2

for i in range(3, n+1) :
    m[i] = i * m[i-1]
    while(m[i]!=0) :
    
        if m[i]%10 != 0: # 뒤의 0 은 더 곱해도 0 이므로 사전에 지워버리자
            break
        m[i]//=10
    m[i]%=1000000000000 # 더 작은 수로 나타내기 위해 10^12 로 나머지 연산을 하자

fact = m[n]
# print(fact)

while(fact!=0) :
    
    if fact%10 != 0:
        break
    fact//=10

ans = str(fact % 100000)

ans = ''.join(['0' for i in range(0, 5-len(ans))]) + ans
print(ans)
# print(ans[len(ans) -5 :])
    
