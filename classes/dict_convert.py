from abc import ABC, abstractmethod


class DictConvert(ABC):
    @abstractmethod
    def get_dict(self):
        pass
