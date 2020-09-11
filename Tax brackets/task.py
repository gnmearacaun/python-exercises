# Round your calculated_tax to the nearest integer.
# Sample Input: 14378
# The tax for 14378 is 0%. That is 0 dollars!
# 0 — 15,527: 0% tax
# 132,407 and more: 28% tax

# income = int(input('Please enter your income in dollars: '))
income = int(input())

if income <= 15527:
    percent = 0
    calculated_tax = int(round(income * (percent / 100)))

# 15,528 — 42,707: 15% tax
elif 15528 <= income < 42708:
    percent = 15
    calculated_tax = int(round(income * (percent / 100)))

# 42,708 — 132,406: 25% tax
elif 42708 <= income <= 132406:
    percent = 25
    calculated_tax = int(round(income * (percent / 100)))

else:
    percent = 28
    calculated_tax = int(round(income * (percent / 100)))

print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
