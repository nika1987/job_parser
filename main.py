from pprint import pprint
from container import vacancy_service


def main():
    while True:
        command = input("Чтобы получить список всех вакансий введите 'все вакансии' , \n"
                        "Для поиска по ключевому слову введите 'поиск вакансий'\n"
                        "Чтобы получить список top 10 вакансий введите 'топ вакансий' \n"
                        "Чтобы получить список вакансий c максимальной зарплатой введите 'максимальная зарплата'\n"
                        "Чтобы получить список вакансий c минимальной зарплатой введите 'минимальная зарплата' \n"
                        "Чтобы записать список вакансии в файл введите 'сохранить все' \n"
                        "Чтобы записать последний результат сортировки в файл введите "
                        "'сохранить результат' \n"
                        "Чтобы выгрузить список вакансий из файла 'загрузить из файла'"
                        "\nДля завершения работы введите команду 'выход': \n"
                        ).lower()
        if command == "все вакансии":
            vacancies = vacancy_service.get_all_vacancies()
            vacancy_titles = [vacancy.get('title') for vacancy in vacancies]
            pprint(
                f"Вакансии загружены успешно: {', '.join(vacancy_titles)}")

        elif command == "поиск вакансий":
            keyword = input("Введите название профессии: ").lower()
            vacancies = vacancy_service.get_by_keyword(keyword)
            pprint(f"Вакансии загружено успешно: {vacancies}")
        elif command == "топ вакансий":
            top = input("Сколько вакансий хотите получить: ")
            vacancies = vacancy_service.get_top_vacancies(int(top))
            pprint(f"Вакансии загружены успешно: {vacancies}")
        elif command == "максимальная зарплата":
            vacancies = vacancy_service.get_max_salary()
            pprint(f"Вакансии загружены успешно: {vacancies}")
        elif command == "минимальная зарплата":
            vacancies = vacancy_service.get_min_salary()
            pprint(f"Вакансии загружены успешно: {vacancies}")
        elif command == "сохранить все":
            vacancies = vacancy_service.save_all_vacancies()
            pprint(f"Вакансии сохранены успешно: {vacancies}")
        elif command == "сохранить результат":
            vacancies = vacancy_service.save_last_result()
            pprint(f"Вакансии сохранены успешно: {vacancies}")
        elif command == "загрузить из файла":
            vacancies = vacancy_service.get_from_json()
            pprint(vacancies)
        elif command == "выход":
            pprint("До свидания")
            break
        else:
            pprint("Неизвестная команда")


if __name__ == "__main__":
    main()
