from GeometricProgressionClass import GeometricProgression
from FibonacciProgressionClass import FibonacciProgression

# Part Two
print("Part Two: Geometric Progression Sum")
r_value = float(input("What number between -1 and 1 not including 0 would you like for your r?"))
start_value = float(input("What starting value do you want not including 0?"))
expected_value = 1 / (1 - r_value)

test_progression = GeometricProgression(r_value, start_value)
sum = start_value
print(sum)
while sum < expected_value - .00001 or sum > expected_value + .00001:
    sum += test_progression._advance()
    print(sum)

# Part Three

fib_test = FibonacciProgression()
number_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in range(500):
    fib_test._advance()
    current_num = str(fib_test.get_current())
    first_num = int(current_num[0])
    number_count[first_num] += 1

print()
print("Part Three: Fibonacci Count")
print(number_count)
