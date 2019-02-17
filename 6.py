sumOfSq = 0
sqOfSum = 0

for i in range(1, 101):
    sumOfSq += i * i
    sqOfSum += i

print((sqOfSum * sqOfSum) - sumOfSq)
