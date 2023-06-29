def findindex(arr):
    low=0
    high=len(arr)-1

    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid

        elif arr[mid-1]<arr[mid]:
            low=mid+1
        elif arr[mid-1]>arr[mid]:
            high=mid-1

def findlh(arr,low,high,ele):
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        elif ele<arr[mid]:
            high=mid-1

        elif arr[mid]<ele:
            low=mid+1
    return -1

def findrh(arr,low,high,ele):
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        elif ele>arr[mid]:
            high=mid-1
        elif ele<arr[mid]:
            low=mid+1
    return -1





def findele(arr,ele):
    index=findindex(arr)

    lh=findlh(arr,0,index,ele)
    rh=findrh(arr,index+1,len(arr)-1,ele)

    if lh!=-1:
        return lh
    elif rh!=-1:
        return rh
    else:
        return -1

arr=[1,2,3,4,20,8,7,6,3]
print(findele(arr,20))