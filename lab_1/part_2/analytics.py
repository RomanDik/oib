import original_text
import key_2 as key
import logging


def analytics(text: str) -> list:
    """
    Функция возращает список пар - буква и её частота появления в тексте.
    :param text:
    :return list:
    """
    dictonary_of_frequency = {}
    len_text = len(text)
    try:
        for letter in text:
            if (letter not in dictonary_of_frequency.keys()):
                frequency = text.count(letter) / len_text
                dictonary_of_frequency[letter] = frequency
            else:
                continue
        result = sorted(dictonary_of_frequency.items(), key=lambda x: x[1], reverse=True)
        return result
    except Exception:
        logging.error(f"Ошибка в функции analytics(text): не удалось вернуть список")


if __name__ == "__main__":
    message = original_text.text
    dictonary1 = analytics(message)
    print(dictonary1)

    for letter in key.dictonary:
        message = message.replace(key.dictonary[letter], letter)

    print(message)