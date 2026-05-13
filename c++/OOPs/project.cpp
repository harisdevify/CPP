#include <iostream>
#include <string>

using namespace std;

// 1. ABSTRACTION: An Abstract Class (Interface)
// This is a blueprint. You cannot create an object of 'BasePayment'.
class BasePayment {
public:
    // Pure Virtual Function makes this class "Abstract"
    virtual void processPayment(double amount) = 0;
    virtual ~BasePayment() {} // Virtual destructor for safety
};

// 2. ENCAPSULATION & INHERITANCE
class BankAccount : public BasePayment {
private:
    double balance; // Private: Hidden data (Encapsulation)

protected:
    string transactionID; // Protected: Shared with child classes

public:
    // --- CONSTRUCTOR ---
    BankAccount(double initialBalance) {
        balance = initialBalance;
        transactionID = "TXN000";
        cout << "[Constructor] Account Initialized." << endl;
    }

    // --- DESTRUCTOR ---
    ~BankAccount() {
        cout << "[Destructor] Account Session Ended." << endl;
    }

    // Helper method to access private balance
    double getBalance() { return balance; }

    void setBalance(double b) { balance = b; }
};

// 3. POLYMORPHISM: Different classes using the same function name
class CreditCard : public BankAccount {
public:
    CreditCard(double bal) : BankAccount(bal) {}

    // Overriding the function (Polymorphism)
    void processPayment(double amount) override {
        transactionID = "CC-123";
        if (amount <= getBalance()) {
            setBalance(getBalance() - amount);
            cout << "Paid $" << amount << " via Credit Card. ID: " << transactionID << endl;
        }
    }
};

class PayPal : public BankAccount {
public:
    PayPal(double bal) : BankAccount(bal) {}

    // Overriding the function differently (Polymorphism)
    void processPayment(double amount) override {
        transactionID = "PP-999";
        double fee = 5.0; // PayPal takes extra fee
        if ((amount + fee) <= getBalance()) {
            setBalance(getBalance() - (amount + fee));
            cout << "Paid $" << amount << " via PayPal (+$5 fee). ID: " << transactionID << endl;
        }
    }
};

int main() {
    // Using Polymorphism with Pointers
    BasePayment* payment1 = new CreditCard(1000.0);
    BasePayment* payment2 = new PayPal(1000.0);

    cout << "--- Transactions ---" << endl;
    payment1->processPayment(100.0); // Runs CreditCard logic
    payment2->processPayment(100.0); // Runs PayPal logic

    delete payment1; // Destructor called
    delete payment2; // Destructor called

    return 0;
}
