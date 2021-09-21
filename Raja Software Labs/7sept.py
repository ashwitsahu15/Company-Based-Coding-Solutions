# def frequencyOfNumericChars(n) :
#     arr=[0]*10
#     ans=[]
#     for i in n :
#         m=ord(i)
#         if m>=48 and m<=57 :
#             arr[m-48]+=1
#     others=len(n)-sum(arr)
#     for i in range(len(arr)) :
#         if arr[i]>0 :
#             print(str(i),end='')
#             print("=",end="")
#             print(arr[i])
#     print("others=",end='')
#     print(others)

# frequencyOfNumericChars("Buffet101")
def x(s) :
    arr=[x for x in s.split('.')]
    for i in range(len(arr)) :
        if i%2!=0 :
            arr[i]='xyz'
    print(*arr,sep='.')
x("i.like.this.program.very.much")

# def secondMaxDiff(numbers):
#     n1,n2=0,0
#     cnt=len(numbers)
#     for i in range(cnt-1):
#         for j in range(i+1,cnt):
#             n=abs(numbers[i]-numbers[j])
#             if n>n1:
#                 n1,n2=n,n1
#             elif n>n2:
#                 n2=n
#     return n2


# def isprime(n) :
#     if n<=1 :
#         return False 
#     for i in range(2,n) :
#         if n%i==0 :
#             return False
#     return True
# def prime(n) :
#     flag1=0
#     flag2=0    
#     ans1=0
#     ans2=0
#     (a,b)=(n,n)
#     while(flag1==0 or flag2==0) :
#         a=a+1
#         b=b-1
#         if isprime(a) and flag1==0:
#             ans1=a
#             flag1=1
#         if isprime(b) and flag2==0 :
#             ans2=b
#             flag2=1
#     if (ans1-n)==(n-ans2) :
#         return ans2,ans1
#     elif (ans1-n)<(n-ans2) :
#         return ans1
#     else :
#         return ans2
# print(prime(32))
# print(prime(30))
def getFibOutput(input) :
    a=0
    b=1
    s=0
    while(b<=input) :
        if(b==input) :
            return input
        s+=b
        b+=a
        a=b-a
    return s
print(getFibOutput(21))
print(getFibOutput(20))