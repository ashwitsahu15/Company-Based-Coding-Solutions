# n=int(input())
# m=n
# ans=0
# while n>0 :
#     ans+=n%10
#     n=n//10
# if m%ans==0 :
#     print("Yes")
# else :
#     # print("No")

# n=int(input())
# arr=[]
# for i in range(n) :
#     arr.append(int(input()))
# j=0
# while j<n :
#     maxi=0
#     for i in range(n) :
#         if i!=j :
#             maxi=max(maxi,arr[i])
#     j+=1
#     print(maxi)


n=int(input())
s=input()
d={}
for i in s :
    if i not in d :
        d[i]=1
    else :
        d[i]+=1
arr2=[]
arr1=[]
for i in d :
    while d[i]!=0 :
        if d[i]>n :
            d[i]-=1
            arr2.append(i)
        elif d[i]<n :
            d[i]-=1
            arr2.append(i)
        else :
            arr1.append(i)
            break
arr1.sort()
arr2.sort()
arr1=arr1*2
print(*arr1,*arr2,sep='')