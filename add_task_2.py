def digit_root(num):
    # Проверка на ограничение по величине числа
    if num > 10**7:
        return None
    # Проверка что число состоит из одной цифры 
    while num > 9:
        sum_digits = 0
        for digit in str(num):
            sum_digits += int(digit)
        num = sum_digits
    return num
number = int(input("Введите число для вычисления цифрового корня: "))
result = digit_root(number)

if result == None:
    print("Ошибка: число слишком большое")
else:
    print(f"Цифровой корень числа {number} равен {result}")

