import requests
from managers.base import BaseParser
from managers.classes import Vacancy


class HeadHunterAPI(BaseParser):
    def __init__(self, url: str, vacancy: type[Vacancy] = Vacancy):
        """
        Инициализация класса HeadHunterAPI
        """

        super().__init__(url, vacancy)
        self._url = url
        self._vacancy = vacancy
        self._params = {
            "per_page": 100
        }

    def get_from_api(self) -> list[Vacancy]:
        """
        Метод для загрузки данных с внешнего API
        :return: возвращает данные по API в виде словаря json
        """
        response = requests.get(self._url, params=self._params)
        result = response.json()
        return self._create_models(result['items'])

    def __repr__(self):
        return f"HeadHunterAPI ({self._url})"

    def _create_models(self, data: list[dict]) -> list[Vacancy]:
        """
        Метод для создания списка экземпляров класса Vacancy
        """
        vacancies = []
        for item in data:
            try:
                vacancy = self._vacancy(id=item['id'], title=item['name'], url=item['alternate_url'],
                                   payment_from=item['salary']['from'], payment_to=item['salary']['to'],
                                   description=item['snippet']['responsibility'], city=item['area']['name'])
                vacancies.append(vacancy)
            except Exception as e:
                print(f"Возникла ошибка {e}")

        return vacancies

    def get_by_keyword(self, keyword: str) -> list[Vacancy]:
        """
        Метод для поиска вакансий по ключевому слову
        """
        self._params['text'] = keyword
        response = requests.get(self._url, params=self._params)
        self._params.pop('text')
        result = response.json()
        return self._create_models(result['items'])

#var1 = HeadHunterAPI(HH_URL)
#result = var1.get_from_api()
#pprint(result)
