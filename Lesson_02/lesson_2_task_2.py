def dev_by_four(number):
    return "True" if number % 4 == 0 else "False"

num = int(input("Введите число: "))
result = dev_by_four(num)
print(f"Год {num}? - {result}")