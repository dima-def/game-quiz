print('Привет! Это прогграмма для записи характеристик ваших машин!')

car = {
    'ower': '',
    'brand': '',
    'color': '',
    'hp': 0,
    'state number': ''
}


name = input('Введите имя владельца:')
car['ower'] = name

brand = input('Введите марку машны:')
car['brand'] = brand

color = input('Введите цвет машины:')
car['color'] = color

hp = input('Введите лошадиные силы:')
car['hp'] = hp

number = input('Введите гос. номер:')
car['state number'] = number

print('Окей, итак вы записали  свою машину. Теперь вы можете вывести данные о ней')

num = input('Нажмите\n1 если ходите вывести имя владельца или добавить другого,\n2 если марку,\n3 если цвет,\n4 если лошадиные силы,\n5 если гос. номер\n')


def changes(car, input_text, field, field_text, print_text):
    answer = input(input_text)
    if answer == 'да':
        new_value = input(field_text)
        car[field] = new_value
    elif answer == 'нет':
        print(print_text, car[field]) 


if num == '1':
    changes(
        car,
        'Хотите переименовать владельца?',
        'ower',
        'Введите имя владельца:',
        'Имя владельца:'
    )
elif num == '2':
    changes(car, 'Хотите изменить марку? (да/нет)', 'brand', 'Введите марку машины:', '')
elif num == '3':
    changes(car, 'Хотите изменить цвет? (да/нет)', 'color', 'Введите цвет машины:', '')
elif num == '4':
    changes(car, 'Хотите изменить лошадиные силы? (да/нет)', 'hp', 'Введите лошадиные силы:', '')
elif num == '5':
    changes(car, 'Хотите изменить гос. номер? (да/нет)', 'state number', 'Введите гос. номер:', '')
