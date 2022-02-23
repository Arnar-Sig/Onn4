#include <iostream>
#include <vector>
#include <utility>
#include <stdio.h> 
#include <iostream>
using namespace std;




int knap(int capacity, int length,  vector<int> weights, vector<int> values){
    vector<vector<int>> storage(length+1, vector<int>(capacity+1));
    for(int i=0; i < length+1; i++){
        for(int thyngd=0; thyngd < capacity; thyngd++){
            if(i == 0 || thyngd == 0){
                storage[i][thyngd] = 0;
            }
            else if(weights[i-1] <= thyngd){
                storage[i][thyngd] = max(storage[i-1][thyngd], values[i-1] + storage[i-1][thyngd - weights[i-1]]
                );
            }
            else{
                storage[i][thyngd = storage[i-1][thyngd]];
            }
        }
    }
    
    int thyngd = capacity;
    int curr = storage[length][capacity];
    int count = 0;
    vector<int> indices;

    for(int i=length; i>0 && curr >= 1; i--){
        if (curr == storage[i-1][thyngd]){
            continue;
        }
        else{
            thyngd = thyngd - weights[i-1];
            curr = curr - values[i-1];
            count = count + 1;
            //cout << "pusha i-1: i indices:" << i-1 << endl;
            indices.push_back(i-1);
        }
    }
    cout << count << endl;
    for(int i : indices){
        cout << i << " ";
    }
    return 0;
}


int main(){
    int C, n;
    while (cin >> C >> n){
       
        
        vector<int> weights;
        vector<int> values;
        
        int thyngdStak, valueStak;
        int count = 0;
        for(int i=0; i<n; i++){
            cin >> valueStak >> thyngdStak;
            values.push_back(valueStak);
            weights.push_back(thyngdStak);
        }
        knap(C, n, weights, values);
        










    }
}
