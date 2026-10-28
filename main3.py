age=int(input("Ваш возраст:"))
if age >= 18:
    print("Добро пожаловать к нам в клуб!")
else:
    print("Извините ваш возраст не подходит! Вход строго с 18!")



temperature=int(input("Сколько сейчас градусов на улице?"))
if temperature < 0:
    print("Очень холодно! Надень тёплую куртку!")
elif temperature >= 0 and temperature <= 10:
    print("Прохладно. Возьми шапку!")
elif temperature >= 11 and temperature <= 20:
    print("Нормально. Куртка подойдёт.")
elif temperature > 20:
    print("Тепло! Лёгкая одежда — в самый раз.")