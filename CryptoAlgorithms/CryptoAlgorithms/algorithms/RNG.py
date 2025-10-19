import time
from CryptoAlgorithms.helpers.numbers import gcd

m = 2 ** 24

# Генератор псевдослучайных чисел
class RNG:

     #Параметр по умолчанию

    def __init__(self):

        # В качестве случайной величины берется unix timestamp
        self.a = int(time.time()) % m
        mod = self.a % 4

        # Проверка на то, что остаток равен 1
        match mod:
            case 0:
                self.a = self.a + 1
            case 2:
                self.a = self.a - 1
            case 3:
                self.a = self.a + 2

        # Так же время, но добавлены какие-то случайные математические величины
        self.b = (int(time.time()) + 43054 - 3167) % m

        # Необходимо, чтобы были взаимно простыми
        # Если это не так, то генерируем число заново
        while gcd(self.b, m) != 1:
            self.b = (int(time.time()) + 43054 - 3167) % m

        self.c_0 = int(time.time() * 1234) % m

    # Метод генерации числа
    def generate(self, previous):
        return (self.a * previous + self.b) % m

    # Метод генерации последовательности чисел.
    # Добавляем c_0 в массив значений и расширяем его новыми числами
    # По окончанию - берем срез всего массива кроме первого элемента
    # Если первый элемент так же нужен в итоговой последовательности, то просто возвращаем весь массив
    def generate_sequence(self, count):
        values = [self.c_0]
        for i in range(count):
            values.append(self.generate(values[i]))
        return values[1::]

    # Загрузка генератора по уже готовым параметрам
    @staticmethod
    def load_from_params(a, b, c_0):
        rng = RNG()
        rng.a = a
        rng.b = b
        rng.c_0 = c_0
        return rng