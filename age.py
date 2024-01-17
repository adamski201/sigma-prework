import datetime

def convert_to_iso_datetime(date):
    return datetime.date.fromisoformat(date)

def calculate_date_delta(date):
    iso_date = convert_to_iso_datetime(date)
    current_date = datetime.date.today()
    delta = current_date - iso_date
    return delta.days // 365

print("Please enter a date in the format YYYY-MM-DD.")

user_date = input("Enter here: ")

delta_years = calculate_date_delta(user_date)

print(f"The difference between the provided date and today is {delta_years} year(s) (rounded down).")


