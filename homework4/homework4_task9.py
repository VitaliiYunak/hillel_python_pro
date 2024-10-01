class DynamicProperties:
    def __init__(self):
        self.__properties = {}

    def add_property(self, name, default_value=None):
        """
        Додає динамічну властивість з геттером та сеттером.
        """
        self.__properties[name] = default_value

        # Геттер
        def getter(self):
            return self.__properties[name]

        # Сеттер
        def setter(self, value):
            self.__properties[name] = value

        setattr(self.__class__, name, property(getter, setter))


if __name__ == "__main__":
    obj = DynamicProperties()
    obj.add_property('name', 'default_name')

    print(obj.name)  # default_name

    obj.name = "Python"
    print(obj.name)
