def findlowerindex(arr):
    low=0
    high=len(arr)-1
    c=arr[-1]
    while(low<=high):
        mid=low+(high-low)//2

        nex=(mid+1)%len(arr)
        prev=(mid-1+len(arr))%len(arr)

        if arr[mid]<arr[prev] and arr[mid]<arr[nex]:
            return arr[mid]

        elif arr[mid]>c:
            low=mid+1
        elif arr[mid]<c:
            high=mid



def findnooftimes(arr):

    index=findlowerindex(arr)
    print(index)
    ro=(len(arr)-index)%len(arr)
    print(arr[ro])
    print('no of rotation is',ro)

arr=[4,5,6,7,8,1,2,3]
findnooftimes(arr)


nums = [4,5,6,7,0,1,2]
findnooftimes(nums)

arr=[5,1,2,3,4]
findnooftimes(arr)

arr=[1,2,3,4]
findnooftimes(arr)

