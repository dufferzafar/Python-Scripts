balance = 3926
annualInterestRate = 0.2

for minPayment in range(10, 1000, 10):

    bal = balance
    flag = 0

    for i in range(1,13):
        # Your unpaid balance
        uBal = bal - minPayment

        # The new balance
        bal = uBal + (uBal * annualInterestRate/12.0)

        # Has the balance been paid?
        if (bal <= 0):
            flag = 1
            break

    # We have what we need, now let's get the fuck out of here...
    if flag:
        break

print("Lowest Payment: " + str(minPayment))
