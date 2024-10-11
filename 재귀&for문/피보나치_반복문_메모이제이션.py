n = int(input())

m = [-1 for _ in range(46)]
m[0] = 0
m[1] = 1

for i in range(2, n+1) :
    m[i] = m[i-1] + m[i-2]

print(m[n])

# for 문
# recursion error 발생할 때
