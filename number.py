import random

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