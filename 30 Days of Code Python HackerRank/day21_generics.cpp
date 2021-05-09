// köken
// date: 28.04.2021 (dd/mm/yyyy)
// there was no python version, so this one is in C++
// used the reference below
// reference: https://github.com/zfields/HackerRank/blob/master/Contests/30%20Days%20of%20Code%20Challenges/Day%2021:%20Generics.cpp
// also check this one for more info: http://www.cplusplus.com/doc/oldtutorial/templates/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename t>
void printArray (vector<t> v_) {
    for (auto &element : v_) {
        cout << element << endl;
    }
}

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
