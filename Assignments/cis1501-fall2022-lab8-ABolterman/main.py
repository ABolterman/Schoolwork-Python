import os
import datetime
import random

curr_day = datetime.date(2022, 10, 15)

num_days = 31
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    if not os.path.exists(os.path.join('logs', year, month, day)):
        os.makedirs(os.path.join('logs', year, month, day))

    file_path = os.path.join('logs', year, month, day, 'log.txt')

    f = open(file_path, 'w')
    for j in range(random.randint(50, 100)):
        f.write(f"{random.randint(1, 7) + (random.randrange(0, 95, 5) / 100):.2f}\n")

    curr_day = curr_day + datetime.timedelta(days=1)

# then ask the user if they want total sales from the last day, last 7 days or last 30 days,
# read the sales data from the files and total it for the user.
# calculate average sales for the day, and the period
choice = int(input("How many days back do you want sales data for? 1/7/30?"))
day_totals = {}
curr_day = datetime.date(2022, 11, 13)
for i in range(choice):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)
    file_path = os.path.join('logs', year, month, day, 'log.txt')
    file = open(file_path)
    data = file.readlines()
    total = 0
    number_of_sales = 0
    for line in data:
        line = line.strip("\n")
        total += float(line)
        number_of_sales += 1
    day_totals[f"{year}/{month}/{day}"] = [total, number_of_sales, total / number_of_sales]

    curr_day = curr_day - datetime.timedelta(days=1)
total_sale_amount = 0
total_sale_count = 0
average_sale_per_day = {}
for key in day_totals:
    total_sale_amount += day_totals[key][0]
    total_sale_count += day_totals[key][1]
    average_sale_per_day[key] = (f"${day_totals[key][2]:.2f}")

print(f"The total sales for the last {choice} days is ${total_sale_amount:.2f}.")
print(f"The average number of sales per day is {total_sale_count /choice:.2f}.")
print(f"The average sale amount over the last {choice} days is ${total_sale_amount / total_sale_count:.2f}.")
print(f"The average sale amount per day is:")
print(average_sale_per_day)