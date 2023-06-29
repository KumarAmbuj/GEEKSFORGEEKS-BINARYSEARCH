def findbs(arr,ele):

    low=0
    high=len(arr)-1

    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        if ele<arr[mid]:
            low=mid+1
        elif ele>arr[mid]:
            high=mid-1

    return -1

arr=[90,89,78,70,48,39,30,20,10]
print(findbs(arr,90))
print(findbs(arr,78))
print(findbs(arr,10))
print(findbs(arr,48))
print(findbs(arr,59))
print(findbs(arr,69))
