def calculate_balance(initial_balance, deposit, withdraw):
    total = initial_balance + deposit
    total_balance = total - withdraw
    return total_balance

    name = input("Enter name: ")
    initial_balance = int(input("Enter initial balance: "))
    deposit = int(input("Enter deposit amount: "))
    withdraw = int(input("Enter withdrawal amount: "))

    total = initial_balance + deposit
    total_balance = calculate_balance(initial_balance, deposit, withdraw)
    
    print("\nName:",name)
    print("\nInitial Balance:", initial_balance)
    print("Deposit Amount:", deposit)
    print("Total:", total)
    print("Withdrawal Amount:", withdraw)
    print("Total Balance:", total_balance)