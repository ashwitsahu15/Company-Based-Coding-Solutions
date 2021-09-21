def nextLargerElement(arr,n):
    s=[]
    for i in range(len(arr)):
        while s and s[-1].get("value") < arr[i]:
            d = s.pop()
            arr[d.get("ind")] = abs(d.get("ind")-i)
        s.append({"value": arr[i], "ind": i})
    while s:
        d = s.pop()
        arr[d.get("ind")] = n
    return arr




for _ in range(int(input())) :
    n=int(input())
    s=input()
    ans=0
    lb=[0]*n
    rb=[0]*n
    temp=-1
    for i in range(n) :
        if(s[i]=='1') :
            temp=i
        else :
            lb[i]=abs(temp-i)
    rb=nextLargerElement(list(s),n)
    for i in range(n) :
        if s[i]=='0' :
            ans+=min(lb[i],rb[i])

    print("Case #"+str(_+1)+": "+str(ans))
        

    # ans=0
    # if s.count('1')==n :
    #     print("Case #"+str(_+1)+": "+'0')
    # else :
    #     for i in range(n) :
    #         if s[i]=='1' :
    #             arr.append(i)
    #     for i in range(n) :
    #         mini=10e5
    #         if s[i]=='0' :
    #             for j in arr :
    #                 mini=min(mini,abs(i-j))
    #             ans+=mini
    #     print("Case #"+str(_+1)+": "+str(ans))