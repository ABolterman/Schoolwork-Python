import random
from CarQueueClass import CarQueue
from FryStackClass import FryStack

drive_thru_line = CarQueue()
available_fries = FryStack()
cook_time = 0
costs = 0
revenue = 0
cars_came = 0
cars_served = 0


for minute in range(60):
    new_car = random.randint(1, 3)
    if new_car == 1:
        cars_came += 1
        drive_thru_line.enqueue()

    if drive_thru_line.get_length() != 0:
        for i in range(drive_thru_line.get_order()):
            if available_fries.get_length() != 0:
                if available_fries.peek_stack() <= 10:
                    revenue += 1
                    available_fries.pop()
                    drive_thru_line.decrease_order()
                else:
                    for fry in range(available_fries.get_length()):
                        available_fries.pop()
        if drive_thru_line.get_order() == 0:
            drive_thru_line.dequeue()
            cars_served += 1

    available_fries.cooking_done(cook_time)
    costs, cook_time = available_fries.drop_fries(costs, drive_thru_line, cook_time)

    cook_time += 1
    for fry in available_fries.storage:
        available_fries.age_fries()

print(f"Revenue:    {revenue} \n"
      f"Costs:      {costs} \n"
      f"Profit:     {revenue-costs} \n")
print(f"Cars Served: {cars_served} / {cars_came}")

