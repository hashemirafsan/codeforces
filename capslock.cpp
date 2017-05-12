#include <iostream>

using namespace std;

int main() {

    string s;

    int l = 0;
    int h = 0;

    cin >> s;

    for(int i = 0; i < s.size(); i++) {
        char a = s[i];
        if(islower(a) == 2) {
            if(i == 0) {
                l++;
            }
        } else {
            h++;
        }
    }
    if(l == 1 && h == s.size() - 1) {
        s[0] = (char) toupper(s[0]);
        for(int i = 1; i < s.size(); i++){
            s[i] = (char) tolower(s[i]);
        }
        cout << s << endl;
    } else if(h == s.size()) {
        for(int i = 0; i < s.size(); i++){
            s[i] = (char) tolower(s[i]);
        }
        cout << s << endl;
    } else {
        cout << s << endl;
    }

}
