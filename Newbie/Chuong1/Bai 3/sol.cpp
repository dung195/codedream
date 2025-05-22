#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pq priority_queue
#define bs binary_search
#define int ll
const ll sized = 3005;
const ll N = 1e7;
const ll inf = 1e18;
const ll MOD = 123456789;
const ll LOG = 20;

main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    freopen("PNEXP.inp","r",stdin);
	freopen("PNEXP.out","w",stdout);
    float a,b;
    cin>>a>>b;
    cout<<setprecision(2)<<fixed<<a+b<<endl;
    cout<<setprecision(2)<<fixed<<a-b<<endl;
    cout<<setprecision(2)<<fixed<<a*b<<endl;
    cout<<setprecision(2)<<fixed<<a/b<<endl;
    return 0;
}
