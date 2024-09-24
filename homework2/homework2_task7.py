total_expense = 0


def add_expense(costs):
    global total_expense
    total_expense += costs
    print(f"Додано витрати у сумі {costs}.\nЗагальна сума витрат: {total_expense}.")


def get_expense():
    return total_expense


def expense_menu():
    while True:
        print("1. Додати витрати")
        print("2. Загальна сума витрат")
        print("3. Завершити роботу")

        choice = input("Виберіть опцію (1-3): ")

        if choice == '1':
            try:
                costs = float(input("Введіть суму витрат: "))
                if costs < 0:
                    print("Сума витрат не може бути < 0.")
                else:
                    add_expense(costs)
            except ValueError:
                print("Введіть коректну суму.")
        elif choice == '2':
            print(f"Загальна сума витрат: {get_expense()}.")
        elif choice == '3':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір.")


expense_menu()
