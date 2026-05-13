#include <iostream>
#include <fstream>
using namespace std;
int main(){
  // ios::app -> always writes data at the end of file (append mode)
  // ios::ate -> opens file and moves pointer to end, but you can move pointer anywhere after that

  fstream file("example.txt", ios::in | ios::out | ios::ate);
  file.seekg(0); // move pointer to beginning of file
  file<< "HELLO"; // write to file
  file.close();
  return 0;
}
