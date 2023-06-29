def findbs(arr,low,high,ele):
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            return mid

        if ele<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

def findelement(arr,ele):
    low=0
    high=1

    while(arr[high]<ele):
        low=high
        high=2*high


    index=findbs(arr,low,high,ele)
    print(index)

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
findelement(arr,22)