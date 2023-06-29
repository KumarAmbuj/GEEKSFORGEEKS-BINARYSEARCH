def findfloorceil(arr,ele):
    low=0
    high=len(arr)-1
    floor=-1
    ceil=-1
    while(low<=high):
        mid=low+(high-low)//2

        if arr[mid]==ele:
            floor=ele
            ceil=ele
            return floor,ceil

        elif arr[mid]<ele:
            floor=arr[mid]
            low=mid+1
        elif arr[mid]>ele:
            ceil=arr[mid]
            high=mid-1
    return floor,ceil

def findmindiff(arr,ele):

    floor,ceil=findfloorceil(arr,ele)

    if floor!=-1 and ceil!=-1:
        print(min(abs(floor-ele),abs(ele-ceil)))

    elif floor!=-1:
        print(abs(floor-ele))
    elif ceil!=-1:
        print(abs(ceil-ele))


arr=[1,2,3,4,8,9,10,11,13,18]
findmindiff(arr,5)
findmindiff(arr,6)
findmindiff(arr,22)
