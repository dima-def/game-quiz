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

num = input('Нажмите 1 если ходите вывести имя владельца или добавить другого, 2 если марку, 3 если цвет, 4 если лошадиные силы, 5 если гос. номер')


if num == '1':
    name2 = input('Хотите переименовать владельца?')
    if name2 == 'да':
        name = input('Введите имя владельца:')
        car['ower'] = name
    elif name2 == 'нет':
        print('Имя владельца:', car['ower'])
elif num == '2':
    num3 = input('Хотите изменить марку?')
    if num3 == 'да':
        brand = input('Введите марку машны:')
        car['brand'] = brand
    elif num3 == 'нет':
        print(car['brand'])
elif num == '3':
    num4 = input('Хотите изменить цвет?')
    if num4 == 'да':
        color = input('Введите цвет машины:')
        car['color'] = color
    elif num4 == 'нет':
        print(car['color'])
elif num == '4':
    num5 = input('Хотите изменить лошадиные силы?')
    if num5 == 'да':
        hp = input('Введите лошадиные силы:')
        car['hp'] = hp
    elif num5 == 'нет':
        print(car['hp'])
elif num == '5':
    num6 = input('Хотите изменить гос. номер?')
    if num6 == 'да':
        number = input('Введите гос. номер:')
        car['state number'] = number
    elif num6 == 'нет':
        print(car['state number'])