income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))

savings = income - expenses
print("Your monthly savings are $" + str(savings))

projected_saving = savings * 12 + (savings * 12 * 0.05)
print("Projected savings after one year, with interest is: $" + str(projected_saving))