#include <iostream>
#include <set>
#include <string.h>
#include <vector>
using namespace std;
typedef long long ll;
vector<int> uppl;


int main(){
    int N, K;
    cin >> N >> K;

    vector<int> uppl(N+1, 0);
    vector<int> count(N+1, 0);


    for (int i=0; i<K; i++){
        char stafur;
        ll fyrra;
        ll seinna;
        cin >> stafur >> fyrra;
        
        if(stafur == 'F'){
            int countStaerd = count.size();
            if(uppl[fyrra] == 1){
                //cout << "biti var 1, flippa i 0" << endl;
                uppl[fyrra] = 0;
                int countStaerd = count.size();
                for(int j=fyrra; j<countStaerd; j++){
                    count[j] = count[j] - 1;
                }
            }else{
                //cout << "biti var 0, flippa i 1" << endl;
                uppl[fyrra] = 1;
                for(int j=fyrra; j<countStaerd; j++){
                    count[j] = count[j] + 1;
                }
            }
        }
        else if(stafur == 'C'){
            cin >> seinna;
            int talan = count[seinna] - count[fyrra-1];
            //out << "athuga fjölda ása á bilinu milli " << fyrra << " og " << seinna << endl;
            cout << talan << endl; 
        }
    }
}