def findlowerindex(arr):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2

        prev=(mid-1+len(arr))%len(arr)
        nex=(mid+1)%len(arr)

        if arr[mid]<arr[prev] and arr[mid]<arr[nex]:
            return mid

        if arr[mid]>arr[low]:
            low=mid+1
        elif arr[mid]<arr[high]:
            high=mid-1
def lefthalf(arr,ele,low,high):
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        if ele<arr[mid]:
            high=mid-1

        elif ele>arr[mid]:
            low=mid+1
    return -1


def righthalf(arr, ele, low, high):
    while (low <= high):
        mid = low + (high - low) // 2

        if arr[mid] == ele:
            return mid

        if ele < arr[mid]:
            high = mid - 1
        elif ele > arr[mid]:
            low = mid + 1
    return -1


def findelement(arr,ele):

    index=findlowerindex(arr)

    l=lefthalf(arr,ele,0,index-1)
    r=righthalf(arr,ele,index,len(arr)-1)

    if l!=-1:
        print(l)
    elif r!=-1:
        print(r)
    else:
        print('not present')

arr=[4,5,6,7,8,9,1,2,3]
findelement(arr,7)
findelement(arr,2)
findelement(arr,10)