from abc import ABC, abstractmethod


class AbstractVacancyProvClass(ABC):
    """Абстрактный класс для провайдеров вакансий."""

    @abstractmethod
    def get_vacancy(self, vacancy_name:str):
        """Абстрактный метод для получения вакансии по названию."""
        pass
