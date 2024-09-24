subscribers = []


def subscribe(name):
    subscribers.append(name)

    def confirm_subscription():
        return f"Підписка підтверджена для: {name}"

    print(confirm_subscription())


def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        print(f"{name} успішно відписаний(-на)")
    else:
        print(f"Підписника з ім'ям {name} не знайдено")


subscribe("Олена")
subscribe("Ігор")
subscribe("Василій")
print(subscribers)
unsubscribe("Василій")
print(subscribers)
