A=[]#input as per needed bujhijibu hela seithire function ru asuthile so aau lekhini
B=[]#same as above
l = []
for i in B:
    a,b,c=i
    if a == 1:
        A[b-1]=c
    else:
        t=A[b-l:c]
        m=-99999999
        for i1 in range (len(t)+1): 
            for i2 in range (i1+1, len(t)+1):
                h=t[i1:i2]
                ml=0
                for j in range(0, len(h)): 
                    if j%2==0: 
                        ml+=h[j] 
                    else:
                        ml-=h[j]
                m=max(ml,m)
        if m>0:
            l.append(m,1000000007)
        else:
            l.append(1000000007-m)
print(l)