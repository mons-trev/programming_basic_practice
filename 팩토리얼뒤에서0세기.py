# print(0%0) # 0 으로 modular 연산 불가

n = int(input()) 
# 파이썬 최대 정수는 8 byte = 64 bit 이므로 9로 시작하는 19자리 수 가짐
# int 는 4 byte = 32 bit 이므로 2로 시작하는 10자리 수 20억~
# in

memo = [-1 for i in range(501)]

memo[0] = 0
memo[1] = 1

def factorial(n) : # 최대 19 자리 저장 가능
    if n<=2 :
        memo[n]=n
        return memo[n]
    if memo[n] != -1 :
        return memo[n]
    memo[n]=n*factorial(n-1)
    return n*factorial(n-1)
    
    
ans = factorial(n)
ansnum = 0

while(ans != 0 and ans%10==0) :
    ansnum+=1
    ans//=10
print(ansnum)
