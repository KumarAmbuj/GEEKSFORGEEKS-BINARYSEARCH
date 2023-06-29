def findceil(arr,ele):
    low=0
    high=len(arr)-1
    res=-1
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return arr[mid]

        if arr[mid]>ele:
            res=arr[mid]
            high=mid-1
        elif arr[mid]<ele:
            low=mid+1
    return res

arr=[1,2,3,7,8,9]
print(findceil(arr,5))
print(findceil(arr,1.5))