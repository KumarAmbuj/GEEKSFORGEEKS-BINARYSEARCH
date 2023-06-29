def bs(arr,ele):
    low=0
    high=len(arr)-1

    while(low<=high):
        mid=(low+high)//2

        if arr[mid]==ele:
            return mid

        elif ele<arr[mid]:
            high=mid-1

        elif ele>arr[mid]:
            low=mid+1
    return -1

arr=[4,12,33,34,47,89,90]
print(bs(arr,12))
print(bs(arr,90))
print(bs(arr,4))
print(bs(arr,9))


arr=[1,3,5]
print(bs(arr,6))