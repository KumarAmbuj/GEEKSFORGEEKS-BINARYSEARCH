def findfloor(arr,ele):
    low=0
    high=len(arr)-1
    res=-1
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]<ele:
            res=arr[mid]
            low=mid+1
        elif arr[mid]>ele:
            high=mid-1

    return res

arr=[1,2,6,7,8]
print(findfloor(arr,5))
print(findfloor(arr,7))