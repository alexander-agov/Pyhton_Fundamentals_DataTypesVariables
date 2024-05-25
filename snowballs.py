
n_balls = int(input())
max_value = 0
best_snowball_show = 0
best_snowball_time = 0
best_snowball_quality = 0
for i in range(n_balls):
    snowball_show = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_show / snowball_time) ** snowball_quality
    if snowball_value > max_value:
        max_value = snowball_value
        best_snowball_show = snowball_show
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print (f"{best_snowball_show} : {best_snowball_time} = {int(max_value)} ({best_snowball_quality})")
