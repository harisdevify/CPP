#include <iostream>
using namespace std;

class myClass{
  private: // private access spacifier
    string day, month, year; // data members

  public: // publi access spacifier
    void function(string a, string b, string c){ // member function
      day=a;
      month= b;
      year= c;
    }
    void showdate(){  // member function
      cout<<"date: "<<day<<':'<<month<<":"<<year<<endl;
    }
};

int main(){
  myClass newClass; // class instantaintion and object/instance
  newClass.function("02", "01", "2026"); // call public member func inside class
  newClass.showdate(); // call public member func inside class

  // newClass.day; // can't access bkz of private access spacifier
  return 0;
}
