import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " + formatted_datetime)

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print("Future date: " + formatted_future_date)

calculate_future_date()