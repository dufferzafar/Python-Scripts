balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

bal = balance
sumPayments = 0

for i in range(1,13):

    # Minimum payment paid
    minPayment = monthlyPaymentRate * bal

    # Sum the payments
    sumPayments += minPayment

    # Your unpaid balance
    uBal = bal - minPayment

    # The new balance
    bal = uBal + (uBal * annualInterestRate/12.0)

    # Let's get this done away with
    print("Month: " + str(i))
    print("Minimum monthly payment: " + str(round(minPayment, 2)))
    print("Remaining balance: " + str(round(bal, 2)))

print("Total paid: " + str(round(sumPayments, 2)))
print("Remaining balance: " + str(round(bal, 2)))
