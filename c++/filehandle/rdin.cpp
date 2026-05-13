#include <iostream>
#include <fstream>
using namespace std;

int main() {

    int id;
    string name;
    string department;
    int salary;

    ifstream file("example.txt");

    if (!file) {
        cout << "Error opening file!" << endl;
        return 1;
    }

    // optional: skip header line
    string line;
    getline(file, line); // line for ignoring header


  while (file >> id>> name>> department>> salary){
    // file >> id >> name >> department >> salary;

    cout << id << "\t"
      << name << "\t"
      << department << "\t" "\t"
      << salary << endl;
    }

    file.close();

    return 0;
}
