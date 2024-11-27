import random
import datetime

start_date_str = '12-11-2024'
end_date_str = '22-11-2024'

start_date_obj = datetime.datetime.strptime(start_date_str, '%d-%m-%Y')
end_date_obj = datetime.datetime.strptime(end_date_str, '%d-%m-%Y')

date_range = end_date_obj - start_date_obj

random_days = random.randint(0, date_range.days)

random_date = start_date_obj + datetime.timedelta(days=random_days)

random_hours = random.randint(0, 23)
random_mins = random.randint(0, 59)
random_secs = random.randint(0, 59)

random_date = random_date.replace(hour=random_hours, minute=random_mins, second=random_secs)

print(f'The random date and time in between {start_date_str} and {end_date_str} is \n{random_date}')