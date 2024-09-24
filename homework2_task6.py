def create_calculator(operator):
    def action(a, b):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "Ділити на нуль не можна."
            return a / b
        else:
            return "Немає такого оператора."

    return action


addition = create_calculator('+')
subtraction = create_calculator('-')
multiplication = create_calculator('*')
division = create_calculator('/')

print(addition(5, 5))
print(subtraction(5, 5))
print(multiplication(5, 5))
print(division(5, 5))
