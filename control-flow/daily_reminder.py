task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes or no):")
priority = input("Priority (high, medium, low):")

match priority:
    case "high":
        status = "high"
    case "medium":
        status = "medium"
    case "low":
        status = "low"

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {status} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {status} priority task. Consider completing it when you have free time.")