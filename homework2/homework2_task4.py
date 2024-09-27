default_time = 60


def training_session(number_rounds):
    """
    Функція приймає кількість раундів.
    Вкладена функція adjust_time використовується для налаштування часу.
    Виводиться інформація про час кожного раунду.
    """
    time_per_round = default_time

    def adjust_time(change_time):
        nonlocal time_per_round
        time_per_round = change_time

    print("Результат:")
    correct_text = ""
    for i in range(1, number_rounds + 1):
        if i > 1:
            correct_text = "(після додавання часу)"
        print(f"Раунд {i}: {time_per_round} хвилин {correct_text}")
        new_time = time_per_round - 5
        adjust_time(new_time)


training_session(3)
