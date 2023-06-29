def bs(arr,ele):
    low=0
    high=len(arr)-1

    while(low<=high):
        mid = low + (high - low) // 2

        if arr[mid] == ele:
            return mid

        if ele < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def findfirst(arr,ele):
    low=0
    high=len(arr)-1
    res=-1

    while low<=high:
        mid=low+(high-low)//2

        if arr[mid]==ele:
            res=mid
            high=mid-1
        elif ele>arr[mid]:
            low=mid+1
        elif ele<arr[mid]:
            high=mid-1
    return res


def findlast(arr, ele):
    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == ele:
            res = mid
            low=mid+1
        elif ele > arr[mid]:
            low = mid + 1
        elif ele < arr[mid]:
            high = mid - 1
    return res

def findfirstandlast(arr,ele):
    if bs(arr,ele)!=-1:
        f = findfirst(arr, ele)
        s = findlast(arr, ele)

        print('first occurrence is ',f)
        print('last occurrence is ',s)
    else:
        print('element not present')


arr=[1,2,3,10,10,10,10,12,15,20,28,29,30]
findfirstandlast(arr,10)
findfirstandlast(arr,4)


