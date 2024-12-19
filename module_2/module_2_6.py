
n = int(input("Введите число от 3 до 20: "))
# n % (x1 + x2) == 0    x1, x2 от 1 до n - 1
full_list = []
result = ''

for x1 in range(1, n):
    for x2 in range(1, n):
        if n % (x1 + x2) == 0 and x1 != x2: # and x1 != x2  не вижу в условиях задачи упоминания о том, что пары с одинаковыми цифрами не подходят
            if ((str(x1) + str(x2)) not in full_list) and ((str(x2) + str(x1)) not in full_list):
                full_list.append(str(x1) + str(x2))
                result += (str(x1) + str(x2))

print(result)
