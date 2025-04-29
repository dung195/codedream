#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pq priority_queue
#define bs binary_search
#define int ll
const ll sized = 1e6;
const ll N = 1e7;
const ll inf = 1e18;
const ll MOD = 123456789;
const ll LOG = 20;
int bang[sized];
int dd[sized];
main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    //freopen("LIS.inp","r",stdin);
	//freopen("LIS.out","w",stdout);
    int n;
    cin>>n;
    for(int i=1;i<=n;i++) cin>>bang[i];
    int now=0;
    for(int i=1;i<=n;i++){
        int k=lower_bound(dd+1,dd+now+1,bang[i])-dd;
        if(k==now+1){
            now++;
            dd[k]=bang[i];
        }
        dd[k]=bang[i];
    }
    cout<<now<<endl;
    return 0;
}
