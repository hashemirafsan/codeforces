#include <iostream>
#include <ctype.h>
using namespace std;

int main() {
    string S,t;
    char c,u;
    int a = 0;
    cin >> S;
    cin >> t;
    for(int i = S.size() - 1; i >= 0; i--) {
        c = S[i];
        u = t[S.size() - (i+1)];
       if(islower(c) == 2 && c == u) {
            a++;
       }
    }

    if(a == S.size()) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }


}
