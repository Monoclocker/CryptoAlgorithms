from CryptoAlgorithms.algorithms.RNG import RNG, m

# Класс состояния приложения
class ApplicationState:

    def __init__(self, generator: RNG):

        self.generator = generator
        self.numbers = [generator.c_0]
        self.sequence = []
        self.time = 0
        self.encrypted_bytes = b''


    # Метод для генерации числа
    def generate_number(self):
        generated = self.generator.generate(self.numbers[0])
        self.numbers.insert(0, generated)

    # Метод для генерации последовательности
    def generate_sequence(self, count):
        self.sequence = self.generator.generate_sequence(count)

    # Метод для обновления времени шифрования
    def update_time(self, time):
        self.time = time
