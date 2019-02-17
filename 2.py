arr = [0, 1]
sum = 0
i = 2
while (arr[len(arr) - 1] < 4000000):
    val = arr[i - 2] + arr[i - 1]
    if val % 2 == 0:
        sum += val
    arr.append(val)
    i += 1
print(arr)
print(sum)
