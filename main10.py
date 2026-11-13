list = ["хлеб", "молоко", "сыр", "колбаса", "кефир" ]
for i in range(5):
    print(list[i])
list.append("банан")
list.remove("кефир")
print("Добавили: банан")
print("Удалили: кефир")
print("Итоговый список:", list)