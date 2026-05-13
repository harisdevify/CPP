#include <iostream>
#include <fstream>
using namespace std;

int main() {

    fstream file("example.txt", ios::in | ios::out | ios::ate);
    file.seekp(0);
    file << "HELLO";
    file.close();

    return 0;
}
