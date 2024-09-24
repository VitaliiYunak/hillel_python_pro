import builtins

lst = [1, 3]


def sum(a, b):
    return "This is my custom sum function!"


print(sum(2, 4))
print(builtins.sum(lst))


# Що відбувається, коли локальна функція має те саме ім'я, що й вбудована?
# Відповідь: Виконується локальна функція

# Як можна отримати доступ до вбудованої функції, навіть якщо вона перекрита?
# Відповідь: Імпортувати модуль builtins та звернутися до функції через builtins.