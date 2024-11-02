print('Добро пожаловать в калькулятор: ')
x = float(input('Введите первое число: '))
action = input('Введите действие: *, -, +, / ')
y = float(input('Введите второе число: '))
print()

print('Ваш пример:', x, action, y)

if action == '*':
    print('Ответ:',x * y)
elif action == '-':
    print('Ответ:',x - y)
elif action == '+':
    print('Ответ:',x + y)
elif action == '/':
    print('Ответ:',x / y)

main = input()