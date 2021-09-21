n=int(input())
arr=[int(x) for x in input().split()]

ans=0
s=[]

rb=[]
s.push(n-1)
rb[n-1]=n
for i in range(n-2) :
    
lb=[-1]

for i in range(n) :
    width=rb-lb-1
    area=arr[i]*width
    ans=max(area,ans)

print(ans)