from managers.classes import Vacancy
from managers.file_storage import FileStorage
from managers.headhunter import HeadHunterAPI
from managers.superjob import SuperJobAPI


class VacancyService:
    def __init__(self, hh_manager: HeadHunterAPI, superjob_manager: SuperJobAPI, filestorage: FileStorage):
        """
        Инициализация класса VacancyService

        :param hh_manager: экземпляр класса HeadHunterAPI.
        :param superjob_manager: экземпляр класса SuperJobAPI.
        :param filestorage: экземпляр класса FileStorage
        """
        self._hh_manager = hh_manager
        self._superjob_manager = superjob_manager
        self._filestorage = filestorage
        self._hh_vacancies = []
        self._superjob_vacancies = []
        self._all_vacancies = []
        self._last_result = []

    def get_all_vacancies(self):
        """
        Метод получает все вакансии из API HeadHunter и SuperJob.

        :return: - list: список словарей, представляющих вакансии.
        """
        self._hh_vacancies.extend(self._hh_manager.get_from_api())
        self._superjob_vacancies.extend(self._superjob_manager.get_from_api())
        self._all_vacancies = self._hh_vacancies + self._superjob_vacancies
        return self._get_serialized(self._all_vacancies)

    def get_by_keyword(self, keyword):
        """
        Метод получает вакансии, содержащие указанное ключевое слово, из API HeadHunter и SuperJob
        :param keyword: ключевое слово для поиска(string)
        :return:- list: список словарей, представляющих вакансии
        """
        self._hh_vacancies.extend(self._hh_manager.get_by_keyword(keyword))
        self._superjob_vacancies.extend(self._superjob_manager.get_by_keyword(keyword))
        self._all_vacancies = self._hh_vacancies + self._superjob_vacancies
        return self._get_serialized(self._all_vacancies)

    def get_top_vacancies(self, count: int = 10):
        """
        Метод  получает топ N вакансий на основе их рейтинга
        :param count: количество топовых вакансий для получения. По умолчанию 10
        :return: список словарей, представляющих топовые вакансии
        """
        self._all_vacancies.sort(reverse=True)
        self._last_result = self._all_vacancies[:count]
        return self._get_serialized(self._last_result)

    def get_max_salary(self):
        """
        Метод получает вакансию с наивысшей зарплатой

        :return:объект вакансии с наивысшей зарплатой
        """
        self._last_result = [
            max(self._all_vacancies, key=lambda x: x.payment_from)
        ]

        return self._get_serialized(self._last_result)

    def get_min_salary(self):
        """
        Метод получает вакансию с наименьшей зарплатой
        :return: объект вакансии с наименьшей зарплатой
        """
        self._last_result = [
            min(self._all_vacancies, key=lambda x: x.payment_from)
        ]
        return self._get_serialized(self._last_result)

    def save_all_vacancies(self):
        """
        Сохраняет все вакансии в JSON-файл
        """
        self.save_to_json(self._all_vacancies)

    def save_last_result(self):
        """
        Сохраняет последний результат сортировки в JSON-файл
        """
        self.save_to_json(self._last_result)

    def save_to_json(self, vacancies: list[Vacancy]):
        """
        Cохраняет все вакансии в JSON-файл с использованием хранилища файлов
        """
        vacancies = self._get_serialized(vacancies)
        self._filestorage.save_to_json(vacancies)

    def get_from_json(self):
        """
        Метод получает все вакансии из JSON-файла с использованием хранилища файлов
        """
        return self._filestorage.get_from_json()

    @staticmethod
    def _get_serialized(vacancies: list[Vacancy]) -> list[dict]:
        return [vacancy.model_dump() for vacancy in vacancies]
