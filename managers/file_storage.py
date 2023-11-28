import json
from managers.base import BaseStorage


class FileStorage(BaseStorage):
    def __init__(self, filename: str):
        """
       Инициализация класса FileStorage
       """
        self._filename = filename

    def _write(self, data: dict | list):
        """
        Метод для записи файла

        """

        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            print("New file created successfully.")

    def _read(self):
        """
        Метод для чтения файла

        """
        try:
            with open(self._filename, encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"При чтение возникла ошибка {e}")
            return []

    def save_to_json(self, vacancy: list[dict]):
        """
        Метод для записи данных в файл json

        """
        self._write(vacancy)

    def get_from_json(self):
        """
        Метод для загрузки данных из файла

        """
        return self._read()
