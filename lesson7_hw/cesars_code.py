from string import ascii_lowercase, ascii_uppercase

US_ALPHABET_LOWER = ascii_lowercase
US_ALPHABET_UPPER = ascii_uppercase
RU_ALPHABET_LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RU_ALPHABET_UPPER = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encode_char(char_to_encode, alphabet, shift):
    """
    Шифрует принимаемые символы в соответствии с алфавитом и сдвигом
    """
    encoded_char_position = (alphabet.find(char_to_encode) + shift) % len(alphabet)
    encoded_char = alphabet[encoded_char_position]
    return encoded_char


def decode_char(char_to_decode, alphabet, shift):
    """
    Расшифровывает принимаемые символы в соответствии с алфавитом и сдвигом
    """
    decoded_char_position = (alphabet.find(char_to_decode) - shift) % len(alphabet)
    decoded_char = alphabet[decoded_char_position]
    return decoded_char


def encode_or_decode(func_for_char, message: str, shift: int) -> str:
    """
    Функция шифрует или расшифровывает входящее сообщение
    в соответствии с установленным сдвигом и положением букв в алфавите.
    Шифр работает на двух языках - русский и английский.
    Шифр учитывает верхний и нижний регистр.
    Шифр сохраняет все символы, не являющиеся буквами.
    """
    encoded_or_decoded_message = []

    for char in message:
        if char in US_ALPHABET_LOWER:
            encoded_or_decoded_message.append(
                func_for_char(char, US_ALPHABET_LOWER, shift)
            )
        elif char in US_ALPHABET_UPPER:
            encoded_or_decoded_message.append(
                func_for_char(char, US_ALPHABET_UPPER, shift)
            )
        elif char in RU_ALPHABET_LOWER:
            encoded_or_decoded_message.append(
                func_for_char(char, RU_ALPHABET_LOWER, shift)
            )
        elif char in RU_ALPHABET_UPPER:
            encoded_or_decoded_message.append(
                func_for_char(char, RU_ALPHABET_UPPER, shift)
            )
        else:
            encoded_or_decoded_message.append(char)

    return "".join(encoded_or_decoded_message)


entered_message = input("Введите сообщение для шифрования: ")
entered_shift = int(input("Введите ключ шифрования: "))

encoded_message = encode_or_decode(func_for_char=encode_char,
                                   message=entered_message,
                                   shift=entered_shift
                                   )
print(encoded_message)

decoded_message = encode_or_decode(func_for_char=decode_char,
                                   message=encoded_message,
                                   shift=entered_shift
                                   )
print(decoded_message)
