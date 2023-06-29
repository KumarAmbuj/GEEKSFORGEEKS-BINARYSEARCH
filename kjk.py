def findindex(arr):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        print('low',low)
        print('high',high)
        mid = low + (high - low) // 2

        print('mid',mid)

        nex = (mid + 1) % len(arr)
        prev = (mid - 1 + len(arr)) % len(arr)

        if arr[mid] < arr[prev] and arr[mid] < arr[nex]:
            return mid

        if arr[mid] > arr[0]:
            low = mid + 1
        elif arr[mid] < arr[0]:
            high = mid - 1
arr=[5,6,7,8,1,2,3]
res=findindex(arr)
print(res)

arr=[4,5,6,7,0,1,2,3]
res=findindex(arr)
print(res)


