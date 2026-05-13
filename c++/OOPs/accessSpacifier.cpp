#include <iostream>
using namespace std;

class BankAccount{
   public:
     string accountHolder = "M Haris";

   protected:
     int accountPIN = 12345;

   private:
     double balance = 5000.00;
};

class AccountSaving: BankAccount{
  public:
    void displayPIN(){
      cout<<"displaing account PIN: "<<accountPIN<<endl;
    }
};



int main(){
  BankAccount myAcc;
  AccountSaving mySavings;

  cout << "--- Accessing Class Members ---" << endl;
  cout << "Holder Name: " << myAcc.accountHolder << endl;
  mySavings.displayPIN();
  cout << "-------------------------------" << endl;
 return 0;
}
