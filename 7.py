num = 1
count = 0
while (count < 10001):
    num += 1
    flag = 0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    if (flag == 0):
        count += 1
print(num)
