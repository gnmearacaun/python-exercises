def final_deposit_amount(*interest, amount=1000):
    for n in interest:
        amount += amount * (float(n) / 100)
    return round(amount, 2)
#   new_amount = 0
#   for i in interest:
#       if i < 1:
#           new_amount = amount
#       if 1 <= i < 2:
#           new_amount = amount * 1.05
#       if 2 <= i < 3:
#           new_amount = new_amount + amount * 1.07
#       if i >= 3:
#           new_amount = new_amount + amount * 1.05
#   return f"{'€'+ round(new_amount, 2)}"
# amnt = 1000
# intr = [5, 7, 4]
# print(final_deposit_amount(*intr, amount=amnt))
