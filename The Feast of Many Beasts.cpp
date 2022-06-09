#include <string>
using namespace std;

bool feast(string beast, string dish){
    cout << "dish: "<< dish << "\n";
    cout << "beast: "<< beast << "\n";
    cout << "first letter beast: "<< beast[0] << "\n";
    cout << "first letter dish: "<< dish[0] << "\n";
    cout << "last letter beast: "<< beast.back() << "\n";
    cout << "last letter dish: "<< dish.back() << "\n";
    return (beast[0] == dish[0] && beast.back() == dish.back());
}