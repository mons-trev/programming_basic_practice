o_arr = [2,4,5,6,8,7,3,10,1,9] # 정렬할 무작위 배열 선언

def selectsort(arr) : # 선택정렬
    for i in range(len(arr)) : # 앞의 것을 기준으로 하나씩 늘려감. i 의 전의 것들은 정렬이 완료된 것
        minidx = i
        for j in range(i+1, len(arr)) : # i 의 뒤의 것들 중 가장 작은 원소를 갖고 있는 인덱스를 반환
            if arr[minidx] > arr[j] :
                minidx = j
        arr[minidx], arr[i] = arr[i], arr[minidx] # i 뒤의 원소 중 가장 작은 것과 i 를 swap
    
    return arr        

print(selectsort(o_arr[:])) # 슬라이싱으로 복사해서 보내자

def selectsort_adv(arr) : # 선택정렬
    for i in range(len(arr)-1, -1, -1) : # 뒤에 것을 기준으로 하나씩 줄여보자. i 의 뒤의 것들은 정렬이 완료된 것
        maxidx = i # i 이전의 값들 중 최대값을 찾아야하니 maxidx 로 저장
        for j in range(0, i) :
            if arr[maxidx] < arr[j] :
                maxidx = j
        arr[maxidx], arr[i] = arr[i], arr[maxidx]
        
    return arr

print(selectsort_adv(o_arr[:]))
    
o_arr = [2,4,5,6,8,7,3,10,1,9] # 정렬할 무작위 배열 선언

# 오름차순

def selectsort(arr) : # 선택정렬
    for i in range(len(arr)) : # 앞의 것을 기준으로 하나씩 늘려감. i 의 전의 것들은 정렬이 완료된 것
        minidx = i
        for j in range(i+1, len(arr)) : # i 의 뒤의 것들 중 가장 작은 원소를 갖고 있는 인덱스를 반환
            if arr[minidx] > arr[j] :
                minidx = j
        arr[minidx], arr[i] = arr[i], arr[minidx] # i 뒤의 원소 중 가장 작은 것과 i 를 swap
    
    return arr        

print(selectsort(o_arr[:])) # 슬라이싱으로 복사해서 보내자

def selectsort_adv(arr) : # 선택정렬
    for i in range(len(arr)-1, -1, -1) : # 뒤에 것을 기준으로 하나씩 줄여보자. i 의 뒤의 것들은 정렬이 완료된 것
        maxidx = i # i 이전의 값들 중 최대값을 찾아야하니 maxidx 로 저장
        for j in range(0, i) :
            if arr[maxidx] < arr[j] :
                maxidx = j
        arr[maxidx], arr[i] = arr[i], arr[maxidx]
        
    return arr

print(selectsort_adv(o_arr[:]))
    
def selectsort_likebubble(arr) : # bubble 처럼 앞 뒤의 것만 고려해서 i 의 뒤 원소 중 가장 작은 원소를 앞으로 하나씩 가져오기
    for i in range(len(arr)-1) : # maxidx 필요없음
        for j in range(len(arr)-1, i, -1) :
            if arr[j] < arr[j-1] :
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(selectsort_likebubble(o_arr[:]))

def selectsort_likebubble_adv(arr) : # 뒤로 보내는 방법
    for i in range(len(arr)-1, 0, -1) :
        for j in range(0, i) :
            if (arr[j+1]<arr[j]) :
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr
print(selectsort_likebubble_adv(o_arr[:]))



