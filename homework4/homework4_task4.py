def create_class(class_name, meth):
    # Створення класу
    new_class = type(class_name, (object,), meth)
    return new_class


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


# Методи передаються у вигляді словника, де ключі — це назви методів, а значення — функції.
methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}


if __name__ == "__main__":
    MyDynamicClass = create_class("MyDynamicClass", methods)

    # Створення об'єкта нового класу
    obj = MyDynamicClass()

    print(obj.say_hello())
    print(obj.say_goodbye())
