# Largest prime factor of number 600851475143
import math


# Returns 1 if the number is prime and 0 if it's not
def isPrime(num):
    num1 = int(num)
    for j in range(2, int(math.sqrt(num))):
        if (num % j == 0):
            return 0
    return 1


num1 = 600851475143
largest = 0

# iterating through 3 to the square root of the number
for i in range(3, int(math.sqrt(num1)), 2):
    if (num1 % i == 0 and isPrime(i)):
        largest = i
print(largest)

