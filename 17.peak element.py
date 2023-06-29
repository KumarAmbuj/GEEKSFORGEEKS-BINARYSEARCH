def findpeak(arr):

    low=0
    high=len(arr)-1

    while(low<=high):
        mid=low+(high-low)//2

        if mid>0 and mid<len(arr)-1:

            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return arr[mid]

            elif arr[mid-1]<arr[mid]:
                low=mid+1

            elif arr[mid-1]>arr[mid]:
                high=mid-1
        elif mid==0:
            if arr[mid]>arr[mid+1]:
                return arr[mid]
            else:
                return arr[mid+1]
        elif mid==len(arr)-1:
            if arr[mid]>arr[mid-1]:
                return arr[mid]
            else:
                return arr[mid-1]
arr=[5,10,20,15]
print(findpeak(arr))

