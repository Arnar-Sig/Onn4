#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dp[2005][2005];

void knap(ll cap, ll len, vector<ll> &w, vector<ll> &vals) {
    for(ll ind = 0; ind <= len; ++ind) {
        for(ll thy = 0; thy <= cap; ++thy) {
            if(ind == 0 || thy == 0) dp[ind][thy] = 0;
            else if(w[ind - 1] <= thy) {
                dp[ind][thy] = max(vals[ind - 1] + dp[ind - 1][thy - w[ind - 1]], dp[ind - 1][thy]);
            } else {
                dp[ind][thy] = dp[ind - 1][thy];
            }
        }
    }
    ll thy = cap;
    ll curr = dp[len][cap];
    ll count = 0;
    vector<ll> inds;
    for(ll i = len; i > 0; --i) {
        if(curr == dp[i - 1][thy]) continue;
        else {
            thy = thy - w[i - 1];
            curr -= vals[i - 1];
            count++;
            inds.push_back(i - 1);
        }
    }
    cout << count << '\n';
    for(ll x : inds) cout << x << ' ';
    cout << '\n';
}

int main() {
    ll v, w, C, n;
    while(cin >> C >> n) {
        vector<ll> weights, values;
        for(int i = 0; i < n; ++i) {
            cin >> v >> w;
            values.push_back(v);
            weights.push_back(w);
        }
        memset(dp, 0, sizeof(dp));
        knap(C, n, weights, values);
    }
}