from PositionalListedList import PositionalList


some_list = PositionalList()

for number in range(5):
    some_list.add_last(number)

print(len(some_list))

some_list.add_first(0)
