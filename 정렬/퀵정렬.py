o_arr = [3,5,4,6,8,7,2,10,1,9] # 정렬할 무작위 배열 선언

# 오름차순
def quicksort(low, high) :
    
    if low >= high : # 원소가 한개인 경우
        return
    
    pivot = o_arr[low]
    
    left = low+1
    right = high
    
    while(left<=right) :
        while(left <= high and o_arr[left]<= pivot) : # pivot 보다 큰 애를 찾아 떠남
            left += 1
        while(right > low and o_arr[right]>= pivot) : # pivot 보다 작은 애를 찾아 떠남
            right -=1
        
        if (left>right) : # 교차된거면 pivot 을 옮김
            o_arr[right], o_arr[low] = o_arr[low], o_arr[right]
        else : # 아니면 두 집합 원소 맞교환
            o_arr[left], o_arr[right] = o_arr[right], o_arr[left]
      
    quicksort(low, right-1)
    quicksort(right+1, high)

    return
    
quicksort(0, len(o_arr)-1)
print(o_arr)
    
