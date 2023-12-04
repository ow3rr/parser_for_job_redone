from abc import ABC, abstractmethod


class DictConvert(ABC):
    """Абстрактный класс для конвертации в словарь."""
    @abstractmethod
    def get_dict(self):
        """Абстрактный метод для получения словаря."""
        pass
