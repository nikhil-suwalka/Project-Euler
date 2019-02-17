# 906609
def isPalindrome(num):
    if (str(num) == str(num)[::-1]):
        return 1
    return 0


max = 0
for num1 in range(1000, 100, -1):
    for num2 in range(1000, 100, -1):
        prod = int(num1) * int(num2)
        if (isPalindrome(prod) and prod > max):
            max = prod
            break
print(max)
