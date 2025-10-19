class RNGEncryptor:
    
    def __init__(self, generator):
        self.generator = generator

    def encrypt_text(self, plaintext):  # Метод для шифрования текста
        if isinstance(plaintext, str):  # Проверка, если введенная строка - текст
            text_bits = self.text_to_bits(plaintext)  # Преобразование текста в биты
        elif isinstance(plaintext, bytes):  # Проверка, если введенные данные - байты
            text_bits = self.bytes_to_bits(plaintext)  # Преобразование байтов в биты
        else:
            raise ValueError("Input must be string or bytes")

        bits_needed = len(text_bits)  # Определение количества необходимых битов
        numbers_needed = (bits_needed + 23) // 24  # Определение количества чисел, требуемых для генерации последовательности

        random_sequence = self.generator.generate_sequence(numbers_needed)  # Генерация случайной последовательности чисел

        key_bits = ''  # Инициализация строки ключевых битов
        for num in random_sequence:  # Проход по каждому числу в последовательности
            key_bits += self.number_to_bits(num, 24)  # Преобразование числа в 24-битную строку

            if len(key_bits) >= len(text_bits):  # Если длина ключевых битов превышает необходимую длину текста
                break

        if len(key_bits) < len(text_bits):  # Если длина ключевых битов меньше необходимой длины текста
            raise ValueError(f"Not enough random numbers. Need {len(text_bits)} bits, have {len(key_bits)} bits")

        key_bits = key_bits[:len(text_bits)]  # Обрезка ключевых битов до необходимой длины

        encrypted_bits = ''.join(
            str(int(text_bits[i]) ^ int(key_bits[i]))  # Шифрование текста с помощью исключающего ИЛИ
            for i in range(len(text_bits))
        )

        encrypted_bytes = self.bits_to_bytes(encrypted_bits)  # Преобразование зашифрованных битов в байты

        return encrypted_bytes  # Возвращение зашифрованных данных

    @staticmethod
    def text_to_bits(text):
        utf8_bytes = text.encode('utf-8')
        return ''.join(format(byte, '08b') for byte in utf8_bytes)

    @staticmethod
    def bits_to_text(bits):
        byte_array = bytearray()
        for i in range(0, len(bits), 8):
            byte = bits[i:i + 8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        
        try:
            return byte_array.decode('utf-8')
        except UnicodeDecodeError as e:
            raise ValueError(f"Invalid UTF-8 sequence: {e}")

    @staticmethod
    def number_to_bits(num, bit_length=24):
        return format(num, f'0{bit_length}b')

    @staticmethod
    def bits_to_bytes(bits):
        byte_array = bytearray()
        for i in range(0, len(bits), 8):
            byte = bits[i:i + 8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        return bytes(byte_array)

    @staticmethod
    def bytes_to_bits(byte_data):
        return ''.join(format(byte, '08b') for byte in byte_data)