def isvalid(mid,k,arr):
    s=1
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]

        if sum>mid:
            s+=1
            sum=arr[i]
    return s<=k


def allocatepages(arr,k):
    low=max(arr)
    high=sum(arr)

    res=0
    while(low<=high):

        mid=low+(high-low)//2

        if isvalid(mid,k,arr):
            res=mid
            high=mid-1
        else:
            low=mid+1

    return res

arr=[10,20,30,40]
k=2
res=allocatepages(arr,k)
print(res)
