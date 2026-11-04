import random
max_attempts = 10  # Добавили в самое начало, как просили в задании
while True:
    print("Компьютер загадывает - 1")
    print("Друг загадывает - 2")
    print("Выход - 3")
    n = int(input())
    if n == 3:
        break
    if n == 2:
        i = int(input("Друг вводит число: "))
        attempts = 0
        while True:
            m = int(input("Игрок вводит число: "))
            attempts += 1
            if i > m:
                print("Число должно быть больше")
            elif i < m:
                print("Число должно быть меньше")
            else:
                score = max_attempts - attempts
                print("Молодец, ты угадал!")
                print(f"Результат для двух игроков: вы угадали за {attempts} попыток и получили {score} очков!")
                break
            if attempts == max_attempts:
                print("Попытки закончились! Вы проиграли.")
                print("Результат для двух игроков: 0 очков.")
                break
    if n == 1:
        i = random.randint(1, 100)
        print("Компьютер загадал число от 1 до 100. У вас 10 попыток!")
        attempts = 0
        while True:
            m = int(input("Игрок вводит число: "))
            attempts += 1
            if i > m:
                print("Число должно быть больше")
            elif i < m:
                print("Число должно быть меньше")
            else:
                score = max_attempts - attempts
                print("Молодец, ты угадал!")
                print(f"Результат для одного игрока: вы угадали за {attempts} попыток и получили {score} очков!")
                break
            if attempts == max_attempts:
                print(f"Попытки закончились! Компьютер загадал число {i}. Вы проиграли.")
                print("Результат для одного игрока: 0 очков.")
                break