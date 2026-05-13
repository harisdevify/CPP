#include <iostream>
using namespace std;


class Test {
  public:
    int add(int a, int b){
        return a + b;
    }
    double add(double a, double b, int c){
        return a + b + c;
    }
};


class Animal {
    public:
      virtual void sound(){
          cout << "Animal Sound" << endl;
       }
};

class Cat : public Animal{
  public:
  void sound(){
    cout << "Meow" << endl;
  }
};

int main(){
    Animal* a;
    a = new Cat();
    a->sound();
    return 0;
}
