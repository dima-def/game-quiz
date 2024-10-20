import random

print('Добро пожаловть в гениратор паролей:')
pass_len = int(input('Выбирете пожалуйста сколько символов в пароле: 4, 8 или 16'))

if pass_len < 4:
    print('Ошибка!')
    sys.exit()
if pass_len > 4 and pass_len < 8:
    print('Ошибка!')
    sys.exit()
if pass_len > 8 and pass_len < 16:
    print('Ошибка!')
    sys.exit()
if pass_len > 16:
    print('Ошибка!')
    sys.exit()
        
for i in range(pass_len):
    print(random.randint(0, 9),end='')