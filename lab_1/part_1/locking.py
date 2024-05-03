import os
import json
import logging
from constant import path
import key as key
import read


def get_position(letter: str) -> tuple:
    """
    Функция возращает индекс строки и столбца буквы из матрицы шифра.
    :param letter:
    :return tuple:
    """
    try:
        for i in range(0, len(key.key_matrix)):
            for j in range(0, len(key.key_matrix[0])):
                if (letter == key.key_matrix[i][j]):
                    return i, j
    except Exception as e:
        logging.error(f"Ошибка в функции get_position(letter): {e}")


def locking(message: str) -> str:
    """
    Функция шифрует переданное сообщение используя шифр "квадрат Полибия".
    :param message:
    :return str:
    """
    message = message.lower()
    result = ""
    try:
        for letter in message:
                place_of_letter = get_position(letter)
                result += str(place_of_letter)
        return result
    except Exception as e:
        logging.error(f"Ошибка в функции encryption(message): {e}")


def send_locked_text() -> None:
    """
    Функция считывает сообщение из переданного пользователем файла, шифрует его и записывает в новый файл, заданным пользователем.
    :param :
    :return None:
    """
    try:
        json_data = read.read_file(path)

        if json_data:
            folder = json_data.get("folder", "")
            path_from = json_data.get("path_from", "")
            path_to = json_data.get("path_to", "")

        if folder and path_from and path_to:
            try:
                with open(f"{path_from}", "r", encoding="utf-8") as file:
                    message = file.read()
                    encrypted_text = locking(message)

                with open(f"{path_to}", "w", encoding="utf-8") as file:
                    file.write(encrypted_text)

                print("Текст успешно зашифрован и сохранен в файле.")

            except FileNotFoundError:
                print("Один из файлов не найден.")

            except Exception as e:
                print(f"Произошла ошибка в функции send_locked_text: {e}")

    except Exception as e:
        print(f"Произошла ошибка в функции send_locked_text: {e}")


if __name__ == "__main__":
    send_locked_text()