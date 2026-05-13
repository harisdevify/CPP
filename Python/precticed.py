def even_or_odd(n):
  return 'Even' if n % 2 == 0 else 'Odd'

while True:
  n = int(input("Enter a Number: "))
  print("Result: ", even_or_odd(n))

  again = input("Do you want to start" \
  " again? Yes/No: ").lower()

  if again != 'yes':
    print('Good Bye')
    break


# =====================================



def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/':
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
    else:
        return "Invalid operator! Please use only +, -, *, /."
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Enter the operator (+, -, *, /): ")

        print("Result:", calculator(a, b, op))

    except ValueError:
        print("Please enter valid numbers.")

    again = input("Do you want to calculate again? yes or no: ").lower()
    if again != 'yes':
        print("Goodbye!")
        break



# =====================================


def calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
    return "Invalid operator!"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator: ")

    print("Result:", calculator(a, b, op))

except ValueError:
    print("Please enter valid numbers.")








low =1
high =100

for _ in range(7):
  guess = (low + high)//2
  print(f"Is it {guess}?")

  feedback = input("Enter 'h' if higher, 'l' if" \
  "lower, 'c' if correct: ")

  if feedback == 'h':
    low = guess +1
  elif feedback == 'l':
    high = guess -1
  elif feedback == 'c':
    print("Yay! I guessed It!")
    break
  else:
    print("Invalid Input.")
