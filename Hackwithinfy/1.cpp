//Ashwit r***Į

#include<bits/stdc++.h>
using namespace std;
#define int long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ff first
#define ss second

const int mod=1e9+7;

int n;
vector<int> arr,pre,suf;

void getPreSuff() {

pre.resize(n,-1);
suf.resize(n,n);

stack<int> s;

for(int i=0;i<n;i++) {

while (!s.empty() && arr[i]<=arr[s.top()]) s.pop();

if(!s.empty()) pre[i]=s.top();

s.push(i);

}

while(!s.empty()) s.pop();

for(int i=n-1;i>=0;i--) {

while (!s.empty() && arr[i]<=arr[s.top()]) s.pop();

if(!s.empty()) suf[i]=s.top();

s.push(i);

}
}
int solve() {

getPreSuff();

int ans=0;

for(int i=0;i<n;i++) 
{ int x=suf[i]-pre[i]-1; 
x*= arr[i]; 
ans= max(x, ans);

// cout<<x<<" ";

}

return ans;
}

signed main() {

cin>>n; 
arr.resize(n);
for(int &i: arr) cin>>i;


cout<<solve();

}