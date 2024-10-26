print('Привет!\n Как дела?')

affairs = input('')

affairs = affairs.lower()

if affairs == 'хорошо' or affairs == 'хорошо!' or affairs == 'отлично' or affairs == 'отлично!':
    print('Я рад что у тебя все хорошо')
elif affairs == 'нормально' or affairs == 'нормально!' or affairs == 'сойдет':
    print('Выбери что тебя беспокоит: \n "Учеба", "Работа", "Просто устал(а)"')