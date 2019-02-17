# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 21
sum = 0
while 1:
    for i in range(16, 21):
        if (num % i != 0):
            sum = 0
            break
        else:
            sum += 1

    if (sum == 10):
        print(num)
        break
    num += 1
