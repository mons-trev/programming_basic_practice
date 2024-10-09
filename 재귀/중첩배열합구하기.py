arr = [1,2,[4,5,6],3,4,5,[3,4]]

def rec(arr, idx) :
    
    if(idx==len(arr)) :
        return 0
    
    if type(arr[idx])==int :
        return arr[idx] + rec(arr, idx+1);
    if type(arr[idx])==list :
        return rec(arr[idx], 0) + rec(arr, idx+1)


print(rec(arr, 0))

#37
#다중배열 재귀로 합 구하기
