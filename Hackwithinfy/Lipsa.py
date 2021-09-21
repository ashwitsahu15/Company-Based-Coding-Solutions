# n=input()
# def frequencyOfNumericChars(n) :
#     arr=[0]*9
#     for i in n :
#         m=ord(i)
#         print(i)
#         print(m)
#         if m>=49 and m<=57 :
#             arr[m-49]+=1
#     for i in range(len(arr)) :
#         if arr[i]!=0 :
#             return str(i+1)+' =',arr[i]



# def x(s) :
#     arr=[x for x in s.split('.')]
#     for i in range(len(arr)) :
#         if i%2!=0 :
#             arr[i]='xyz'
#     print(*arr,sep='.')
# x("i.like.this.program.very.much")



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


# int getFibOutput(int input) {
#     int a=0,b=1;
#     int s=0;
#     while(b<=input) {
#         if(b==input) return input;
#         s+=b;
#         b+= a; a=b-a;
#     }
#     return s;
# }