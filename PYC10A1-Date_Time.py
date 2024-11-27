from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print(f"Today's date is {today}")
print(f'Current time is {now}')

# data components
print('Date components:')
print(f'Day: {today.day}')
print(f'Month: {today.month}')
print(f'Year: {today.year}')