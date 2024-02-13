class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def name(self):
        return self.name

    def author(self):
        return self.author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть типа int")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self._pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def name(self):
        return self.name

    def author(self):
        return self.author

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Продолжительность книги должна быть типа float.")
        if value <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self._duration}"
