# include <iostream>
# include <stdio.h>

using namespace std;

int mem[11] = { 1, 2, 4, };

int main(void) {
	int num, n;

	for (int i = 3; i < 11; i++) {
		mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3];
	}

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> n;
		cout << mem[n - 1] << "\n";
	}
	return 0;
}