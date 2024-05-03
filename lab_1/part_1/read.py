import json

def read_file(file_path: str) -> dict:
    """
    Функция считывает данные из JSON файла.
    :param file_path:
    :return dict:
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            return json_data
    except json.JSONDecodeError:
        print("Ошибка считывания данных.")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")