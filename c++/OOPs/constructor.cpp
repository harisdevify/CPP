#include <iostream>
using namespace std;

class Person {
  public:
    int a,b,c;

    Person(int m, int n) {
       a=m;
       b=n;
    }

  int multiply(){
    int c = a*b;
    return c;
  }

};

int main(){
    Person p(2, 4);
    int res = p.multiply();
    cout<< res<<endl;

 return 0;
}
