import json

from dict_convert import DictConvert
from vacancy import Vacancy
from vacancy_prov_hh import VacancyProvHh
from vacancy_prov_sj import VacancyProvSj


def save_vacancy(vacances: list[DictConvert], filename: str):
    """Созраняет список вакансий в файл"""
    vacances = [i.get_dict() for i in vacances]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(vacances, file, ensure_ascii=False, indent=1)


def get_vacancy(query:str)->list[Vacancy]:
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

    user_input = input("Сохранить результат?(Y-Да, N-Нет.)").lower()
    if user_input == "y":
        save_vacancy(vacances, "vacancy.json")

    user_input = input("Хотите продолжить поиск?(Y-Да, N-Нет.)").lower()
    if user_input.lower() == "n":
        exit