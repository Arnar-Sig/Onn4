#include <iostream>

int geymsla[200][50000];
int meals[200];

int food(int i, int r, int last, int orgKal, int orgFjoldi){
    //std::cout << i << std::endl;
    //std::cout << r << std::endl;
    //std::cout << orgKal << std::endl;
    //std::cout << orgFjoldi << std::endl;
    if (i >= orgFjoldi){
        return 0;
    }
    if(geymsla[i][r] == 0){
        geymsla[i][r] = std::max((food(i+1, r*2/3, r, orgKal, orgFjoldi) + std::min(meals[i], r)), 
                std::max(food(i+1, last, r, orgKal, orgFjoldi), food(i+2, orgKal, r, orgKal, orgFjoldi)));     
    }
    return geymsla[i][r];
}

int main()
{
	int fjoldi;
    int kaloriur;
	std::cin >> fjoldi >> kaloriur;
    for(int i = 0; i < fjoldi; i++){
        std::cin >> meals[i];
    }
    int max = food(0, kaloriur, kaloriur, kaloriur, fjoldi);
    std::cout << max << std::endl;
	return 0;
}
