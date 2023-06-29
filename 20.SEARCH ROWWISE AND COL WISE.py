def findele(arr,ele):
    m=len(arr)
    n=len(arr[0])

    row=0
    col=n-1

    while(row>=0 and row<m and col>=0 and col<n):

        if arr[row][col]==ele:
            return row,col

        elif arr[row][col]<ele:
            row+=1

        elif arr[row][col]>ele:
            col-=1
    return -1,-1

arr=[[10,20,30,40],
     [15,25,35,45],
     [27,29,37,48],
     [32,33,39,50]
     ]
row,col=findele(arr,3)
print(row,col)

