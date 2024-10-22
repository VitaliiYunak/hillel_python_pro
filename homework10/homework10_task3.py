# Задача 3: підрахунок суми чисел у великому масиві

import numpy
import multiprocessing


if __name__ == "__main__":
    array_size = 1000
    large_array = numpy.random.randint(1, 100, array_size)
    print(large_array)

    # Кількість процесів для паралельного обчислення
    num_processes = 2
    # Ділимо масив на частини
    array_part = len(large_array) // num_processes
    print(array_part)

    parts = []
    for i in range(num_processes):
        part = large_array[i * array_part:(i + 1) * array_part]
        parts.append(part)

    # Створюємо процеси
    with multiprocessing.Pool(processes=num_processes) as proc:
        # Обчислюємо суму для кожної частини
        results = proc.map(sum, parts)

    # Обчислюємо загальну суму
    total_sum = sum(results)

    print(f"Total sum: {total_sum}")
