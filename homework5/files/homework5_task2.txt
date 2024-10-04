# 2. Ітератор для генерації унікальних ідентифікаторів

import uuid


class GenerationUUID:
    """
    Ітератор для генерації унікальних ідентифікаторів
    """
    def __iter__(self):
        return self

    def __next__(self):
        """
        Генерує унікальний ідентифікатор
        :return: унікальний ідентифікатор
        """
        return uuid.uuid4()


if __name__ == "__main__":
    generate_uuid = GenerationUUID()
    for _ in range(3):
        print(next(generate_uuid))
