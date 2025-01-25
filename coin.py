import random

print('Привет! Нажми ENTER чтобы бросить монетку!')
a = input('')

b = random.randint(1,2)

if b == 1:
    print('Орёл')
elif b == 2:
    print('Решка')
