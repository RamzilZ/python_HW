def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return ('FzzBuzz')
    elif n % 3 == 0:
        return ('Fizz')
    elif n % 5 == 0:
        return ('Buzz')
    else:
        return (n)

s = input('Введите целое число: ')
n = int(s)
for i in range(1, n+1):
    print(fizz_buzz(i))
