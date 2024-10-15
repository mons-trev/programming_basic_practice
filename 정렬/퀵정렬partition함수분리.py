o_arr = [3,5,4,6,8,7,2,10,1,9] # 정렬할 무작위 배열 선언

# 함수 분리

def partition(l, h) :
    
    pivot = o_arr[l]
    start = l+1
    end = h
    
    while(start<=end) :
        while(start<=h and o_arr[start]<=pivot) :
            start+=1
        while(end>l and o_arr[end]>=pivot) :
            end-=1
        
        if(start<end) : # 교차 전이니 두 개 맞교환
            o_arr[start], o_arr[end] = o_arr[end], o_arr[start]
        else : # 교차함
            o_arr[end], o_arr[l] = o_arr[l], o_arr[end]
            
    return end
    

def QuickSort(l, h) :
    if (l>=h) : # 원소가 한개인 경우
        return
    if(l<h) :
        loc = partition(l,h)
        QuickSort(l, loc-1)
        QuickSort(loc+1, h)
    return

QuickSort(0, len(o_arr)-1)
print(o_arr)
