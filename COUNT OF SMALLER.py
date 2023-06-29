def merge(arr,p,q,r,ans):
    n1=q-p+1
    n2=r-q

    l=[]
    r=[]

    for i in range(0,n1):
        l.append(arr[p+i])

    for i in range(0,n2):
        r.append(arr[q+1+i])


    i=0
    j=0
    k=p
    while(i<n1 and j<n2):
        if l[i][1]<=r[j][1]:
            arr[k]=l[i]
            i+=1
            k+=1
        else:


            arr[k]=r[j]
            j+=1
            k+=1

    while(i<n1):
        arr[k]=l[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=r[j]
        j+=1
        k+=1


def mergesort(arr,p,r,ans):
    if p<r:
        q=(p+r)//2
        mergesort(arr,p,q,ans)
        mergesort(arr,q+1,r,ans)
        m=q+1
        j=q+1
        for i in range(p,q+1):
            while(j<=r and arr[j][1]<arr[i][1]):
                j+=1
            ans[arr[i][0]]+=j-(m)
            print(arr[i][0])


        print(ans)

        merge(arr,p,q,r,ans)

def findsmaller(arr):
    n=len(arr)
    ans=[0 for i in range(n)]
    arr=list(enumerate(arr))

    p=0
    r=n-1

    mergesort(arr,p,r,ans)


arr=[5,2,6,1]
findsmaller(arr)

arr=[-1,-1]
findsmaller(arr)

arr=[5,6,2,1]
findsmaller(arr)
