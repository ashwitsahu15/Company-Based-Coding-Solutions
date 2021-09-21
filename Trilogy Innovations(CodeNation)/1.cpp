#include <bits/stdc++.h>
using namespace std;
int countPairs(int arr[], int n){
   // Count of pairs
   int count = 0;
   for (int i = 0; i < n-1; i++){
      for (int j = i + 1; j < n; j++){
         if(arr[i]%arr[j]==0 || arr[j]%arr[i]==0)
            { count++; }
      }
   }
   return count;
}