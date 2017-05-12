#include <iostream>

using namespace std;

int main() {
    int n;
    string r;
    cin >> n;

    for(int i = 1; i <= n; i++) {
        cin >> r;
        if(r.length() <= 10) {
            cout << r << endl;
        }else {
            cout << r[0] << r.length()-2 << r[r.length()-1] << endl;
        }
    }
}
