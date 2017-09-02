#include <iostream>
using namespace std;

int main() {
	int n, c = 0;

	cin >> n;

	string s;

	cin >> s;

	for(int j = 0; j < n; j++) {
		if(s[j] == s[j+1] && j < n - 1) {
			c++;
		}
	}

	cout << c << endl;
}