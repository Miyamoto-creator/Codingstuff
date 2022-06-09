#include <vector>
using namespace std;

vector<int> countBy(int x, int n){
    int total = n * x;
    vector<int> result;
    for (int i = x; i <= total; i+= x)
        result.push_back(i);
    return result;
}