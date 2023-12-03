import os
import requests

from parser_for_job_redone.classes.abstractvacancyprovclass import AbstractVacancyProvClass
from parser_for_job_redone.vacancy.vacancies import Vacancy

class VacancyProvSj(AbstractVacancyProvClass):
    SJ_API_KEY = os.getenv("SJ_API_KEY")

    def get_vacancy(self, vacancy_name):
        res = requests.get("https://api.superjob.ru/2.0/vacancies/", params={"keyword": vacancy_name},
                           headers={"X-Api-App-Id": self.SJ_API_KEY})
        if res.status_code == 200:
            data = res.json()
            result = []
            for a in data["objects"]:
                salary_from = a.get("payment_from", None)
                salary_to = a.get("payment_to", None)

                new_vacancy = Vacancy(a["profession"], salary_from, salary_to, a["link"])
                result.append(new_vacancy)
            return result
