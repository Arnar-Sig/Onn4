#include <iostream>
#include <set>
#include <string.h>
#include <vector>
using namespace std;
vector<int> items;
vector<int> sizes;


int myFind(int p){
    //cout << "byrja i myFind" << endl;
    //cout << "p: " << p << endl;
    //cout << "items[0]: " << items[0] << endl;
    while(items.at(p) != p){
        //cout << "items[p]: " << items[p] << endl;
        //cout << "p: " << p << endl;
        items.at(p) = items.at(items.at(p));
        p = items.at(p);
    }
    return p;
    //cout << "returna ur myFind" << endl;
}


void myUnion(int p, int q){
    int p_root = myFind(p);
    int q_root = myFind(q);

    if(p_root != q_root){
        if (sizes[p_root] < sizes[q_root]){
            int temp = p_root;
            p_root = q_root;
            q_root = temp;
        }
        items[q_root] = p_root;
        sizes[p_root] = sizes[p_root] + sizes[q_root];
    }
}



// int findSize(int p){
//     cout << "er i findSize" << endl;
//     return sizes[p];
// }




int main(){
    int n, q;
    cin >> n >> q;
    vector<int> items;
    vector<int> sizes;
    for(int i=0; i<100;i++){
        items.push_back(i);
        sizes.push_back(1);
    }
    //count = sizes.size();
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
            myUnion(fyrri-1, seinni);
        }
        else{
            int rot = myFind(fyrri);
            cout << rot << endl;

        }
    }
}
