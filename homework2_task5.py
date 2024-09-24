events = []


def calendar():

    def add_evnt(event):
        events.append(event)
        print(f"Додана подія: {event}")

    def view_evnt():
        if not events:
            print("Немає подій.")
        else:
            print("Перегляд подій:")
            for ev in events:
                print(ev)

    def remove_evnt(event):
        try:
            events.remove(event)
            print(f"Видалена подія: {event}")
        except ValueError:
            print(f"Подія '{event}' не знайдена.")

    return add_evnt, remove_evnt, view_evnt


add_events, remove_events, view_events = calendar()

add_events("24.09.2024 12:00 - Python Pro. Домашки")
add_events("24.09.2024 19:15 - Python Pro")
add_events("25.09.2024 18.00 - Знайомство з компанією «UNITY-BARS»")
add_events("28.09.2024 11:15 - English Elementary")
view_events()
remove_events("25.09.2024 18.00 - Знайомство з компанією «UNITY-BARS»")
view_events()
