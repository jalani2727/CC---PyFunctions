def Over9k(lst):
    sum = 0
    for num in lst:
        sum+= num
        if sum>= 9000:
            break
    return sum


print(Over9k([8000, 900, 120, 5000]))