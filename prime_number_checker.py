num = int(input())
isPrime = True
for divider in range(2, num):
    if num % divider == 0:
        isPrime = False
        break
print(isPrime)