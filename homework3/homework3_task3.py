# 3. to-Compare

class Person:
    """
    Перевіряє осіб, хто старший або молодший за віком.
    Виводить відсортований список осіб за віком.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Порівнює за віком (чи менще)
    def __lt__(self, other):
        return self.age < other.age

    # Порівнює за віком (чи більше)
    def __gt__(self, other):
        return self.age > other.age

    # Порівнює за віком (чи дорівнюють)
    def __eq__(self, other):
        return self.age == other.age

    def __repr__(self):
        return f"Ім\'я: {self.name}, вік: {self.age}"


persons = [
    Person("Наталія", 25),
    Person("Миколай", 27),
    Person("Олена", 32),
]

print(f"{persons[0]} < {persons[1]}:", persons[0] < persons[1])
print(f"{persons[1]} > {persons[2]}:", persons[1] > persons[2])
print(f"{persons[1]} == {persons[2]}:", persons[1] == persons[2])

# sorted_persons= sorted(persons, key=lambda ages: ages.age)
sorted_persons = sorted(persons)
print("Відсортований список за віком:")
for person in sorted_persons:
    print(person)
