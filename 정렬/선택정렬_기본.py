o_arr = [2,4,5,6,8,14,3,100,1] # 정렬할 무작위 배열 선언

def selectsort(arr) : # 선택정렬
    for i in range(len(arr)) : # 앞의 것을 기준으로 하나씩 늘려감. i 의 전의 것들은 정렬이 완료된 것
        minidx = i
        for j in range(i+1, len(arr)) : # i 의 뒤의 것들 중 가장 작은 원소를 갖고 있는 인덱스를 반환
            if arr[minidx] > arr[j] :
                minidx = j
            arr[minidx], arr[i] = arr[i], arr[minidx] # i 뒤의 원소 중 가장 작은 것과 i 를 swap
    
    return arr        
print(selectsort(o_arr[:])) # 슬라이싱으로 복사해서 보내자

# [1, 2, 3, 4, 5, 6, 8, 14, 100]

