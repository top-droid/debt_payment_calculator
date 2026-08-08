from datetime import datetime
from dateutil.relativedelta import *
import numbr

income = int(input("What's your income? "))
expenses = int(input("How high are your basic expenses, excluding debt payments? "))
discretionary_income = income - expenses

if discretionary_income < 1:
    print("You don't have enough money to pay your debt off. You have to either increase your income or lower your expenses.")
    quit()

creditors_info = {}

number_of_creditors = int(input("How many different creditors do you have? "))


for i in range(1, number_of_creditors + 1):
    ordinal_number = numbr.Cast(i, target = "Ordinal Number")
    name_of_creditor = input(f"What is the name of the {ordinal_number} creditor? ")
    monthly_repayment_amount = input(f"How much is your monthly repayment towards {name_of_creditor}? ")
    total_credit_amount = input("How much is required to pay this credit off completely? ")
    # Add a Dictionary item with the following format: 
    # Name of creditor: Monthly repayment amount, total credit amount, 0(Paid months starting from now)
    creditors_info[name_of_creditor] = [int(monthly_repayment_amount), int(total_credit_amount), 0]
print(f"Information about the creditors: {creditors_info}\n")

# Calculate how many months it will take to settle each credit
for i in creditors_info:
    month_count = 0
    while creditors_info.get(i)[1] > 0:
        creditors_info.get(i)[1] = (creditors_info.get(i)[1] - creditors_info.get(i)[0])
        month_count += 1
    creditors_info.get(i)[2] = month_count

for i in creditors_info:
    print(f"The debt towards {i}, will be settled in {creditors_info.get(i)[2]} months!\n")

# Algorithm that finds the credit that will be fully paid last and how many months it will take.
last_settled_credit_duration = 0
last_settled_credit_name = []
for creditor in creditors_info:
    if creditors_info.get(creditor)[2] > last_settled_credit_duration:
        last_settled_credit_duration = creditors_info.get(creditor)[2]
        last_settled_credit_name.clear()
        last_settled_credit_name.append(creditor)
    elif creditors_info.get(creditor)[2] == last_settled_credit_duration:
        last_settled_credit_name.append(creditor)
    else:
        pass

print(f"The credit towards {last_settled_credit_name} will be the last one the get settled")
print(f"It will take {last_settled_credit_duration} months to be fully paid off")
print()
    
current_date = datetime.now()
final_settlement_date = current_date + relativedelta(months =+ last_settled_credit_duration)

print(f"Your final credit will be paid off in {final_settlement_date.strftime("%B")} {final_settlement_date.strftime("%Y")}")
print(f"That's {last_settled_credit_duration} months from now.")