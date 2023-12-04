from parser_for_job_redone.classes.dict_convert import DictConvert

class Vacancy(DictConvert):
    def get_dict(self):
        """Метод для получения словаря с информацией о вакансии."""
        return {"title": self.title,
                "url": self.url,
                "sallary_to": self.sallary_to,
                "sallary_from": self.sallary_from}

    def __init__(self, title: str, sallary_from: int, sallary_to: int, url: str):
        self._title = title
        self._sallary_from = sallary_from
        self._sallary_to = sallary_to
        self._url = url

    def __str__(self):
        return f'{self._title} от:{self._sallary_from} до:{self._sallary_to}'

    def __repr__(self):
        return str(self)

    @property
    def url(self):
        return self._url

    @property
    def title(self):
        return self._title

    @property
    def sallary_from(self):
        """Зарплата от"""
        return self._sallary_from

    @property
    def sallary_to(self):
        """Зарплата до"""
        return self._sallary_to

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise Exception("Нельзя сравнивать")
        sallary_from1 = self._sallary_from
        sallary_from2 = other._sallary_from
        sallary_to1 = self._sallary_to
        sallary_to2 = other._sallary_to

        if sallary_from1 is None:
            sallary_from1 = sallary_to1
        if sallary_from2 is None:
            sallary_from2 = sallary_to2
        if sallary_to1 is None:
            sallary_to1 = sallary_from1
        if sallary_to2 is None:
            sallary_to2 = sallary_from2

        if sallary_from1 is None and sallary_to1 is None:
            return True
        if sallary_from2 is None and sallary_to2 is None:
            return False

        return sallary_from1 < sallary_from2 or sallary_to1 < sallary_to2

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise Exception("Нельзя сравнивать")
        sallary_from1 = self._sallary_from
        sallary_from2 = other._sallary_from
        sallary_to1 = self._sallary_to
        sallary_to2 = other._sallary_to

        if sallary_from1 is None:
            sallary_from1 = sallary_to1
        if sallary_from2 is None:
            sallary_from2 = sallary_to2
        if sallary_to1 is None:
            sallary_to1 = sallary_from1
        if sallary_to2 is None:
            sallary_to2 = sallary_from2

        if sallary_from1 is None and sallary_to1 is None:
            return True
        if sallary_from2 is None and sallary_to2 is None:
            return False

        return sallary_from1 <= sallary_from2 and sallary_to1 <= sallary_to2

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return False

        return self._title == other._title \
            and self._sallary_from == other._sallary_from \
            and self._sallary_to == other._sallary_to
