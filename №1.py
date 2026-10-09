def task1():
    print("Задание 1: Проверка делимости на 3")
    
    try:
        n = int(input("Введите целое число: "))
    except ValueError:
        print("Ошибка: введено не целое число.")
        return
    
    if n % 3 == 0:
        print(f"Число {n} делится на 3.")
    else:
        print(f"Число {n} не делится на 3.")


if __name__ == "__main__":
    task1()