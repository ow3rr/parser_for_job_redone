from abc import ABC, abstractmethod


class AbstractVacancyProvClass(ABC):

    @abstractmethod
    def get_vacancy(self, vacancy_name:str):
        pass
