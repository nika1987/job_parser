from abc import ABC, abstractmethod
import requests


response = requests.get('https://api.hh.ru/vacancies')


class BaseParser(ABC):
    @abstractmethod
    def __init__(self, url: str, vacancy):
        pass

    @abstractmethod
    def get_from_api(self):
        pass

    @abstractmethod
    def get_by_keyword(self, keyword):
        pass


class BaseStorage(ABC):

    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def save_to_json(self, data: list[dict]):
        pass

    @abstractmethod
    def get_from_json(self):
        pass
