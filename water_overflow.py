number_of_line = int(input())
sum_of_liters = 0
for i in range(1, number_of_line+1):
    liters = int(input())
    sum_of_liters += liters
    tank_capacity = 255
    if sum_of_liters > tank_capacity:
        print("Insufficient capacity!")
        sum_of_liters -= liters
    continue
print(sum_of_liters)

