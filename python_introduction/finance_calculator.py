monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $" + str(monthly_savings))

projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest is: $" + str(projected_saving))