def findindex(arr):
    res=-1
    low=0
    high=len(arr)-1

    while(low<=high):
        
        mid=low+(high-low)//2

        if arr[mid]==1:
            res=mid
            high=mid-1
        elif arr[mid]==0:
            low=mid+1
    return res

arr=[0,0,0,0,0,0,1,1,1,1,1,1]
print(findindex(arr))