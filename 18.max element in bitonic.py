def findmaxelement(arr):

    low=0
    high=len(arr)-1

    while(low<=high):

        mid=low+(high-low)//2

        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]

        elif arr[mid-1]<arr[mid]:
            low=mid+1
        elif arr[mid-1]>arr[mid]:
            high=mid-1

arr=[1,2,3,4,30,8,7,6,3]
print(findmaxelement(arr))
