def findele(arr,ele):

    low=0
    high=len(arr)-1

    while(low<=high):

        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        if mid-1>=0 and arr[mid-1]==ele:
            return mid-1
        if mid+1<len(arr) and arr[mid+1]==ele:
            return mid+1

        if ele<arr[mid]:
            high=mid-2
        elif ele>arr[mid]:
            low=mid+2
    return -1

arr=[5,10,30,20,40]
print(findele(arr,20))
print(findele(arr,30))
print(findele(arr,70))