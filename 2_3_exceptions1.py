try:
  sign, a, b = input('Введите действие: ').split()
  assert sign in ['+', '-', '*', '/'], 'Вы ввели неверную операцию'
  a = int(a)
  b = int (b)
  if sign == '+':
    result = a + b
  elif sign == '-':
    result = a - b
  elif sign == '*':
    result = a * b
  else:
    result = a / b
  print(result)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print('Что-то пошло не так...', e)
