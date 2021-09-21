# def compare(n,a,b,c) :
#     for i in range(n) :
#         if a[i]!=b[i] and b[i]!=c[i] and a[i]!=c[i] :
#             return False 
#     return True       
# n=int(input())
# a=input()
# b=input()
# c=input()
# if compare(n,a,b,c) :
#     print("Yes")
# else :
#     print("No")

# n=int(input())
# arr=[int(x) for x in input().split()]
# ans=0
# count=0
# for i in range(n-1) :
#     if arr[i+1]<=arr[i] :
#         count+=1
#     else :
#         count=0
#     ans=max(ans,count)
# print(ans)