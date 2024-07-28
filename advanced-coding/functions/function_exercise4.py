
def pay_bill(expenses, commission=9.8, offer_amount=None):
    global final_payable_price

    total_expenses = sum(expenses)

    if offer_amount is not None and total_expenses > offer_amount:
        commission += 1.2
        commission = total_expenses * (commission/100)
        final_payable_price = total_expenses + commission
    return final_payable_price


expense = [100, 200, 300]
comm = 10
offer_amount = 500

print(pay_bill(expense, comm))           # Without special offer
print(pay_bill(expense, comm, 550))      # With special offer
print(pay_bill(expense))                               # Using default commission without special offer
