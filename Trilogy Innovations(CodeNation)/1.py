# a=[x for x in input().split()]
# print(a)
# ans=[]
# n=len(a)
# for i in a :
#     count=0
#     j=0
#     while j<n :
#         if i%a[j]==0 or a[j]%i==0 :
#             count+=1
#         j+=1
#     ans.append(count-1)
# print(*ans,sep = " ")


a=[int(x) for x in input().split()]
n=len(a)
ans=[0]*n
for i in range(n) :
    j=i+1
    while j<n :
        if a[i]%a[j]==0 or a[j]%a[i]==0 :
            ans[i]+=1
            ans[j]+=1
        j+=1
print(ans)