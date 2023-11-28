from pprint import pprint
import requests
from managers.base import BaseParser
from constants import SUPERJOB_URL, SUPERJOB_CODE, SUPERJOB_TOKEN
from managers.classes import Vacancy


class SuperJobAPI(BaseParser):
    def __init__(self, url: str, vacancy: type[Vacancy] = Vacancy) -> None:
        """
        Инициализация класса SuperJobAPI
        """

        super().__init__(url, vacancy)
        self._url = url
        self._vacancy = vacancy
        self._params = {
            "count": 100

        }
        self._headers = {
            'X-Api-App-Id': SUPERJOB_CODE,
            'Authorization': SUPERJOB_TOKEN
        }

    def get_from_api(self) -> list[Vacancy]:
        """
        Метод для загрузки данных с внешнего API
        :return: возвращает данные по API в виде словаря json
        """
        vacancies = []
        for page in range(5):
            self._params['page'] = page

            response = requests.get(self._url, headers=self._headers, params=self._params)
            result = response.json()
            if result:
                vacancies.extend(result.get('objects', []))
        self._params.pop('page', None)
        return self._create_models(vacancies)

    def _create_models(self, data: list[dict]) -> list[Vacancy]:
        """
        Метод для создания  списка экземпляров класса
        """
        vacancies = []
        for item in data:
            vacancy = self._vacancy(id=item['id'], title=item['profession'], url=item['link'],
                                   payment_from=item['payment_from'], payment_to=item['payment_to'],
                                   description=item['candidat'], city=item['town']['title'])
            vacancies.append(vacancy)
        return vacancies

    def get_by_keyword(self, keyword: str) -> list[Vacancy]:
        """
        Метод поиска вакансий по ключевому слову
        """
        self._params['keyword'] = keyword
        response = requests.get(self._url, headers=self._headers, params=self._params)
        self._params.pop('keyword')
        result = response.json()
        return self._create_models(result)
