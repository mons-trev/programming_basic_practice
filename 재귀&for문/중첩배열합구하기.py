arr = [1,2,[4,5,6],3,4,5,[3,4]]

# 합을 return 으로 전달
def rec(arr, idx) :
    
    if(idx==len(arr)) :
        return 0
    
    if type(arr[idx])==int :
        return arr[idx] + rec(arr, idx+1);
    if type(arr[idx])==list :
        return rec(arr[idx], 0) + rec(arr, idx+1)


print(rec(arr, 0))

# 합을 인자로 전달
def rec2(arr, idx, s) :
    if(idx==len(arr)) :
        return s
        
    if type(arr[idx])==int :
        return rec2(arr, idx+1, s+arr[idx])
    if type(arr[idx])==list :
        return rec2(arr[idx], 0, 0) + rec2(arr, idx+1, s)
        
print(rec2(arr, 0, 0))

# 37
# 37
