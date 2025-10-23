
initial_balance = float(input("Enter Initial Balance (₹): "))
deposit = float(input("Enter Deposit Amount (₹): "))

new_balance = initial_balance + deposit
print("Initial Balance: ₹", initial_balance)
print("Deposit: ₹", deposit)
print("New Balance after deposit: ₹", new_balance)

withdraw = float(input("Enter Withdraw Amount (₹): "))

if withdraw > new_balance:
    print("Insufficient Balance!")
else:
    final_balance = new_balance - withdraw
    print("Withdraw: ₹", withdraw)
    print("Final Balance: ₹", final_balance)
