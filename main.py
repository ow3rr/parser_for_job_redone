import json

from classes.dict_convert import DictConvert
from vacancy.vacancies import Vacancy
from vacancy.vacancy_prov_hh import VacancyProvHh
from vacancy.vacancy_prov_sj import VacancyProvSj


def save_vacancy(vacancies: list[DictConvert], filename: str):
    """Созраняет список вакансий в файл"""
    vacancies = [i.get_dict() for i in vacancies]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=1)


def get_vacancy(query: str) -> list[Vacancy]:
    """Получает вакансии с обеих платформ"""
    result = []
    super_job = VacancyProvSj()
    had_hanter = VacancyProvHh()
    result.extend(super_job.get_vacancy(query))
    result.extend(had_hanter.get_vacancy(query))
    return result


while True:
    user_input = input("Какая должность Вас интересует: ")
    vacances = get_vacancy(user_input)
    vacances = sorted(vacances, reverse=True)
    for i in vacances:
        print(i)

    user_input = input("Сохранить результат?(Y-Да, N-Нет.): ").lower()
    if user_input == "y":
        save_vacancy(vacances, "vacancy.json")

    user_input = input("Хотите продолжить поиск?(Y-Да, N-Нет.): ").lower()
    if user_input.lower() == "n":
        quit()
