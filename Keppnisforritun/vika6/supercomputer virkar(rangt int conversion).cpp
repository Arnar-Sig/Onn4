#include <iostream>
#include <set>
#include <string.h>
using namespace std;
typedef long long ll;

int main(){
    int N, K;
    cin >> N >> K;

    set<int> mengi;

  

    for (int i=0; i<=K; i++){
        //cout << "Er i umferd " << i << endl;
        //cout << "mengid er eftirfarandi:" << endl;
        // for(auto ele: mengi){
        //     cout << ele << endl;
        // }
        string inntak;
        cin.clear();
        cout.clear();
        getline(cin, inntak);
        


        if(inntak[0] == 'F'){
            //int gildi = int(inntak[1]) - 48;
            int gildi = inntak[2] - 48;
            //cout << "gildi:" << gildi;
            if(mengi.find(gildi) != mengi.end()){
                mengi.erase(gildi);
            }else{
                mengi.insert(gildi);
            }
        }
        else if(inntak[0] == 'C'){
            //cout << i << endl;
            int count = 0;
            int fyrra = (int)inntak[2] - 48;
            int seinna = (int)inntak[4] - 48;
            for(auto ele : mengi){
                if (ele < fyrra){
                    continue;
                }
                if (ele > seinna){
                    break;
                }
                else{
                    count++;
                }
            }
            cout << count << endl; 
        }
    }
}