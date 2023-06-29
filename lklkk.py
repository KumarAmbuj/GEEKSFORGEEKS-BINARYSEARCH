def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)
def fun(hash):
    arr=[]
    for x in hash:
        arr.append(x)
    Quicksort(arr,0,len(arr)-1)
    for x in arr:
        print("{}'s contact:{}, email:{}".format(x,hash[x][0],hash[x][1]))
    if len(hash)==1:
        print("There are 1 contact in the dictionary.")
    elif len(hash)>1:
        if len(hash) == 1:
            print("There are {} contact in the dictionary.".format(len(hash)))











