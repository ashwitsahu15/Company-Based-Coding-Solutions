n=int(input())
arr=[int(x) for x in input().split()]
rb=[0]*n
lb=[0]*n
st=[-1]
top=0
for i in range(n) :
    while st[-1]!=(-1) :
        if st[-1]<arr[i] :
            break
        else :
            st.pop()
    if st[-1]==(-1) :
        lb[i]=-1
    else :
        lb[i]=top-1
    st.append(arr[i])
    top+=1
print(lb)
ans=0
for i in range(n) :
    ans-max(ans,(rb[i]-lb[i]-1))