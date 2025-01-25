import random
<<<<<<< HEAD

print('Привет!')
print('Загадай любое число от 1 до 10, а я его угадаю!')

a = random.randint(0, 10)

print('Ваше число', a)
b = input('')

if b == 'нет':
    print('Ваше число больше', a)
    num1 = input('')
elif b == 'да':
    print('Я угадал!')


if num1 == 'да':
    c = random.randint(a, 10)
    print('Ваше число больше', c)
    num2 = input('')
elif num1 == 'нет':
    d = random.randint(1, a)
=======
min = 1
max = 100

print('Привет. Я угадаю твое загаданое число от',min, 'до', max)

while True:
    a = random.randint(min, max)

    print('Твое число:', a, '?')

    b = input()

    b = b.lower()

    if b == 'да':
        print('Я угадал твое число')
        break
    elif b == 'больше':
        min = a
    elif b == 'меньше':
        max = a


>>>>>>> 3be39142b4f7d2b69ce0f9fc7fa466d4ae190c44
