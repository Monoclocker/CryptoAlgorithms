import time
from CryptoAlgorithms.helpers.numbers import gcd

# Генератор псевдослучайных чисел
class RNG:

    m = 2 ** 24 #Параметр по умолчанию

    def __init__(self):

        # В качестве случайной величины берется unix timestamp
        self.a = int(time.time())
        mod = (self.a % 4) % self.m

        # Проверка на то, что остаток равен 1
        match mod:
            case 0:
                self.a = self.a + 1
            case 2:
                self.a = self.a - 1
            case 3:
                self.a = self.a + 2

        # Так же время, но добавлены какие-то случайные математические величины
        self.b = int(time.time()) + 43054 - 3167

        # Необходимо, чтобы были взаимно простыми
        # Если это не так, то генерируем число заново
        while gcd(self.b, self.m) != 1:
            self.b = (int(time.time()) + 43054 - 3167) % self.m

        self.c_0 = int(time.time() * 1234) % self.m

    # Метод генерации числа
    def generate(self, previous):
        return (self.a * previous + self.b) % self.m

    # Метод генерации последовательности чисел.
    # Добавляем c_0 в массив значений и расширяем его новыми числами
    # По окончанию - берем срез всего массива кроме первого элемента
    # Если первый элемент так же нужен в итоговой последовательности, то просто возвращаем весь массив
    def generate_sequence(self, count):
        values = [self.c_0]
        for i in range(count):
            values.append(self.generate(values[i]))
        return values[1::]