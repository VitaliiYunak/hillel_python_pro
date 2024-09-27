# 5. For built-in functions implementation

class MyFunctions:
    """
    Вираховуються: кількість елементів, сума всіх єлементів та найменший елемент.
    Використовуються магічні методи __len__, __iter__, __getitem__
    """
    def __init__(self, data):
        self.data = data

    # Власна версія функції len()
    def __len__(self):
        count = 0
        for _ in self.data:
            count += 1
        return count

    # Власна версія функції sum()
    def __iter__(self):
        suma = 0
        for i in self.data:
            suma += i
        return suma

    # Власна версія функції min()
    def __getitem__(self):
        if not self.data:
            return "Відсутні елементи"
        min_data= self.data[0]
        for i in self.data[1:]:
            if i < min_data:
                min_data = i
        return min_data

    def __str__(self):
        return f"{self.data}"


dataset = MyFunctions([3, 5, 4, 1, 5, 8])
print(dataset)
print(f"Кількість елементів: {len(dataset)}")
print(f"Сума елементів: {dataset.__iter__()}")
print(f"Мінімальний елемент: {dataset.__getitem__()}")
