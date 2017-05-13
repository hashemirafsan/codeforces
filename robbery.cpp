#include <iostream>

using namespace std;

int main() {
    int a,b,c,n,t=0;

    cin >> a >> b >> c;
    cin >> n;
    int m[n];
    for(int i = 0; i < n ; i++) {
        cin >> m[i];
        if(m[i] == a) {
            t++;
        } else if(m[i] > b && m[i] < c ) {
             t++;
        }
    }
    cout << t << endl;

}
