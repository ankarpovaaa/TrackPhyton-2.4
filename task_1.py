from abc import ABC, abstractmethod
from typing import Optional


class MusicalInstrument(ABC):
    """
    Базовый класс для всех музыкальных инструментов.

    Атрибуты:
        _name (str): Название инструмента (непубличный, чтобы предотвратить прямое изменение)
        _brand (str): Производитель инструмента (непубличный, для контроля через свойства)
        _price (float): Цена инструмента (непубличный, с валидацией)
    """

    def __init__(self, name: str, brand: str, price: float) -> None:
        """
        Инициализация базового инструмента.

        Args:
            name: Название инструмента
            brand: Производитель
            price: Цена (должна быть положительной)

        Raises:
            ValueError: Если цена отрицательная
        """
        self._name = name
        self._brand = brand
        self._price = price if price > 0 else self._raise_price_error()

    @staticmethod
    def _raise_price_error() -> None:
        """Вспомогательный метод для валидации цены."""
        raise ValueError("Цена должна быть положительной")

    @property
    def price(self) -> float:
        """Геттер для цены (инкапсуляция для контроля доступа)."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией."""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

    def play(self) -> str:
        """
        Базовый метод извлечения звука.

        Returns:
            Описание звучания инструмента
        """
        return f"Извлекается звук из {self._name}"

    def tune(self) -> str:
        """
        Настройка инструмента.

        Returns:
            Результат настройки
        """
        return f"{self._name} настроен"

    def __str__(self) -> str:
        """Пользовательское строковое представление инструмента."""
        return f"{self._brand} {self._name} - {self._price} руб."

    def __repr__(self) -> str:
        """Официальное строковое представление для отладки."""
        return f"{self.__class__.__name__}(name='{self._name}', brand='{self._brand}', price={self._price})"


class Guitar(MusicalInstrument):
    """
    Класс гитары, наследующийся от MusicalInstrument.

    Добавляет специфические атрибуты: количество струн и тип гитары.
    """

    def __init__(self, name: str, brand: str, price: float, strings_count: int = 6,
                 guitar_type: str = "акустическая") -> None:
        """
        Расширение конструктора базового класса.

        Args:
            name: Название модели
            brand: Производитель
            price: Цена
            strings_count: Количество струн (по умолчанию 6)
            guitar_type: Тип гитары (акустическая, электрогитара и т.д.)
        """
        super().__init__(name, brand, price)
        self._strings_count = strings_count
        self._guitar_type = guitar_type

    @property
    def strings_count(self) -> int:
        """Количество струн (инкапсулировано для защиты от некорректных значений)."""
        return self._strings_count

    @strings_count.setter
    def strings_count(self, value: int) -> None:
        """Сеттер с проверкой разумного количества струн."""
        if value < 4 or value > 12:
            raise ValueError("Некорректное количество струн для гитары")
        self._strings_count = value

    def play(self) -> str:
        """
        Перегрузка метода play().

        Причина перегрузки: звукоизвлечение на гитаре имеет специфику
        (используются струны, медиатор или пальцы).

        Returns:
            Описание игры на гитаре
        """
        return f"Игра на {self._guitar_type} гитаре {self._brand} {self._name} ({self._strings_count} струн)"

    def tune(self) -> str:
        """
        Наследование метода tune() без изменений.
        Используется базовая реализация.
        """
        return super().tune()

    def change_strings(self, new_strings: str) -> str:
        """
        Новый метод, специфичный для гитары.

        Args:
            new_strings: Тип новых струн

        Returns:
            Результат замены струн
        """
        return f"Струны {new_strings} установлены на {self._name}"

    def __str__(self) -> str:
        """Перегрузка __str__ с добавлением информации о гитаре."""
        return f"{self._guitar_type.capitalize()} гитара: {self._brand} {self._name}, {self._strings_count} струн, цена: {self._price} руб."

    def __repr__(self) -> str:
        """Перегрузка __repr__ с расширенной информацией."""
        return (f"Guitar(name='{self._name}', brand='{self._brand}', price={self._price}, "
                f"strings_count={self._strings_count}, guitar_type='{self._guitar_type}')")


if __name__ == "__main__":
    # Пример использования
    guitar = Guitar("Stratocaster", "Fender", 85000.0, 6, "электро")
    print(guitar)  # __str__
    print(repr(guitar))  # __repr__
    print(guitar.play())  # перегруженный метод
    print(guitar.tune())  # унаследованный метод
    print(guitar.change_strings("Ernie Ball"))  # новый метод