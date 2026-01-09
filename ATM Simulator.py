balance = 10000
PIN = 4567
max_attempts = 3
attempts = 0

# PIN input loop
while attempts < max_attempts:
    try:
        user = int(input("Enter your PIN: "))
    except Exception:
        print("Invalid PIN! Only numbers allowed.")
        continue

    if user == PIN:
        print("Access granted")

        while True:
            print("\nATM Menu:")
            print("1. Balance  2. Deposit  3. Withdraw  4. Exit")
            choose = input("Choose: ")

            if choose == "1":
                print("Your balance:", balance)

            elif choose == "2":
                add_amount = int(input("Enter amount: "))
                balance += add_amount
                print("Deposited! New balance:", balance)

            elif choose == "3":
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    balance -= amount
                    print("Withdrawn! New balance:", balance)
                else:
                    print("Insufficient balance!")

            elif choose == "4":
                print("Thank you!")
                break

            else:
                print("Invalid choice!")

        break  # Exit PIN loop

    else:
        attempts += 1
        print(f"Wrong PIN Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Account locked due to too many wrong attempts!")
