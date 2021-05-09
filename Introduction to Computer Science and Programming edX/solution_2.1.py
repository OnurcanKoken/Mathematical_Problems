"""
19.03.26
onurcan koken
credit card balance calculation
"""

def balance_cal(balance, annualInterestRate, counter):
    counter -= 1
    if counter == 0:
        return balance
    
    monthlyPaymentRate = annualInterestRate / 12.0
    min_monthly_payment = 0.04 * balance
    # where 0.04 is monthly payment rate for min payment
    monthly_unpaid_balance = balance - min_monthly_payment
    updated_balance = monthly_unpaid_balance + (monthlyPaymentRate * monthly_unpaid_balance)
    return balance_cal(updated_balance, annualInterestRate, counter)

balance = 484
annualInterestRate = 0.2
counter = 13 # indicates month
print("Remaining balance: " + str(round(balance_cal(balance, annualInterestRate, counter),2)))