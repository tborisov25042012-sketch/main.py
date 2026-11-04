print("Введите число 0 для выхода")
total=0
while True:
    number = int(input("Введите число"))
    total= number + total
    if number==0:
        break
print("Сумма:")
print(total)