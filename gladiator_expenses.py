lost_fights = int(input())
helmet_price = float(input())
sward_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
if lost_fights / 12 >= 1:
   expenses = (lost_fights // 2) * helmet_price + (lost_fights // 3) * sward_price + (lost_fights // 6) * shield_price + (lost_fights // 12) * armor_price
else:
    expenses = (lost_fights // 2) * helmet_price + (lost_fights // 3) * sward_price + (lost_fights // 6) * shield_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
