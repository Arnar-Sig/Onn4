#include <iostream>
#include <set>
#include <string.h>
#include <vector>
using namespace std;
vector<int> items(100, 1);
vector<int> sizes(100, 1);
int count;


int myFind(int p){
    //cout << "byrja i myFind" << endl;
    //cout << "p: " << p << endl;
    //cout << "items[0]: " << items[0] << endl;
    while(items[p] != p){
        //cout << "items[p]: " << items[p] << endl;
        //cout << "p: " << p << endl;
        items[p] = items[items[p]];
        p = items[p];
    }
    return p;
    cout << "returna ur myFind" << endl;
}


void myUnion(int p, int q){
    cout << "er i myUnion" << endl;
    if (p == q){
        return;
    }
    //cout << "error 2" << endl;
   
    int p_root = myFind(p);
    //cout << "error 3" << endl;

    int q_root = myFind(q);
    //cout << "error 4" << endl;

    if(p_root != q_root){
        if (sizes[p_root] < sizes[q_root]){
            int temp = p_root;
            p_root = q_root;
            q_root = temp;
        }
        items[q_root] = p_root;
        sizes[p_root] = sizes[p_root] + sizes[q_root];
    }
    count = count - 1;
}



int findSize(int p){
    cout << "er i findSize" << endl;
    return sizes[p];
}




int main(){
    int n, q;
    cin >> n >> q;
    vector<int> items;
    vector<int> sizes;
    for(int i=0; i<=n;i++){
        items.push_back(i);
        sizes.push_back(1);
    }
    count = sizes.size();
    // for(int i=0; i<sizes.size(); i++){
    //     cout << sizes[i] << endl;
    // }


    for(int i=0; i<q; i++){
        //cout << "vectors items og sizes:" << endl;
        // for(int j=0; j<n; j++){
        //     cout << items[j] << endl;
        // }
        // for(int j=0; j<n; j++){
        //     cout << sizes[j] << endl;
        // }
        char stafur;
        int fyrri;
        cin >> stafur >> fyrri;
        if(stafur == 't'){
            int seinni;
            cin >> seinni;
            myUnion(fyrri-1, seinni-1);
        }
        else{
            cout << findSize(myFind(fyrri-1)) << endl;

        }
    }
}
