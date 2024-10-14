o_arr = [2,4,5,6,8,7,3,10,1,9] # 정렬할 무작위 배열 선언

# 오름차순
def insertionsort(arr) :
    for i in range(1, len(arr)) : # 맨 앞의 원소부터 시작할 필요 없음
        for j in range(i, 0, -1) :
            if arr[j]<arr[j-1] :
                arr[j], arr[j-1] = arr[j-1], arr[j]
                
    return arr
    
print(insertionsort(o_arr[:]))


def insertionsort_break(arr) :
    for i in range(1, len(arr)) : # 맨 앞의 원소부터 시작할 필요 없음
        for j in range(i, 0, -1) :
            if arr[j]<arr[j-1] :
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else :
                break # break 문 걸어주기
                
    return arr

print(insertionsort_break(o_arr[:]))
