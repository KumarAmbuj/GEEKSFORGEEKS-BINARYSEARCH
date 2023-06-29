def findnextalphabet(s,ele):
    low=0
    high=len(s)-1
    res=''

    while(low<=high):

        mid=low+(high-low)//2

        if s[mid]>ele:
            res=s[mid]
            high=mid-1
        else:
            low=mid+1
    return res

s='abcdfgh'
res=findnextalphabet(s,'b')
print(res)


