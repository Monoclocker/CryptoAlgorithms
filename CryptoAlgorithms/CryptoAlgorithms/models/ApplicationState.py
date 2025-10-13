from numbers import Number

from CryptoAlgorithms.algorithms.RNG import RNG

class ApplicationState:

    def __init__(self, generator: RNG):

        self.generator = generator
        self.numbers = [generator.c_0]

    def add_number(self, number: Number):
        self.numbers.append(number)

    def generate_number(self):
        generated = self.generator.generate(self.numbers[-1])
        self.numbers.append(generated)

    def generate_sequence(self, count):
        return self.generator.generate_sequence(count)

    def get_distribution(self):
        intervals = [0] * 100
        interval_length = self.generator.m // 100

        for num in self.numbers:
            index = num // interval_length
            intervals[min(index, 99)] += 1

        intervals = [freq / len(self.numbers) for freq in intervals]
        mean_freq = sum(intervals) / len(intervals)

        return mean_freq
