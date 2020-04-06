# получить выражение
# разделить символы
# выделить аргументы - первый и второй
# согласно первому операнду - произвести вычисление, к первому прибавить второй, из первого вычесть второй и т.д.
# проверить, есть ли операция в списке доступных с помощью assert
#
ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}
x = input ('Введите выражение ')
y = x.split()
try:
    for key, values in ops.items():
        if y[0] == key:
            print (values (int(y[1]), int(y[2])))
    assert y[0] in ops.keys(), 'Операции, соответствующей такому операнду не предусмотрено'
except ZeroDivisionError:
    print ('Ошибка деления на ноль')
except ValueError:
    print ('Произошёл ввод строки, а не числа')
except AssertionError as e:
    print ('Непредусмотренная операция')
    print (e)