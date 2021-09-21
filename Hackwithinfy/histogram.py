n=int(input())
hist=[int(x) for x in input().split()]
s=[-1]
n=len(hist)
ans=0
left_boundary=[-1]*n
right_boundary=[n]*n
i=0
while i<n :
    while (s[-1]!=-1) and (hist[s[-1]] > hist[i]) :
        right_boundary[s[-1]] = i
        s.pop()
    if ((i>0) and (hist[i]==hist[i-1])) :
        left_boundary[i]=left_boundary[i-1]
    else :
        left_boundary[i]=s[-1]
    s.append(i)
    i+=1
for j in range(n):
    ans = max(ans,hist[j]*(right_boundary[j]-left_boundary[j]-1))
print(ans)