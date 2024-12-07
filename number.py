import random
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


