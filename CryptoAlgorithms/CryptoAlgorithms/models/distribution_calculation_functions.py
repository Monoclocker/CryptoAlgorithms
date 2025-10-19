from CryptoAlgorithms.algorithms.RNG import m

def get_labels():
    interval_length = float(m) / float(100)
    return [f"{int(i * interval_length)}-{int(i * interval_length + interval_length)}" for i in range(100)]

def get_default_distribution():
    return [0] * 100


def get_distribution(numbers):
    # Инициализируем массив интервалов длиной 100 элементами
    intervals = [0] * 100

    # Если список чисел пустой, возвращаем распределение из начальный список
    if not numbers:
        return intervals

    # Вычисляем длину одного интервала
    interval_length = m / 100

    for num in numbers:
        # Определяем индекс интервала для текущего числа
        index = int(num / interval_length)
        # Если индекс выходит за пределы массива, устанавливаем его в последний элемент
        index = min(index, 99)
        # Увеличиваем счетчик в соответствующем интервале
        intervals[index] += 1

    # Вычисляем относительные частоты для каждого интервала
    frequencies = [count / len(numbers) for count in intervals]

    return frequencies
