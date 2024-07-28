
def pay_bill(expenses, commission=0.098, special_offer=None):

    total_bill = 0
    for amount in expenses:
        total_bill = total_bill + amount

    add_commission = 0
    if special_offer:
        if total_bill >= special_offer:
            add_commission = 0.012
            print("You earned 1.2% extra commission!")

    commission = total_bill * (commission + add_commission)
    final_bill = total_bill - commission
    print(round(final_bill))
    return final_bill


(pay_bill([500, 450, 567, 322], commission=0.1, special_offer=1500))
