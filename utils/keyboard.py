from utils.goods import Goods


class Mixin():
    """Класс Mixin для реализации атрибута __language
    и метода change_language для смены его значения.
    _language - защищенный атрибут (protected).
    Для него определены геттер и сеттер.

    Методы:
    - change_lang - метод смены раскладки (значения language). 
    Возвращает значение текущей раскладки
    - __init__  - инициализация класса
    - change_lang- метод меняет раскладку клавиатур EN на RU
        и наоборот. Возвращает текущее значение раскладки.
        Попытка установить какое-либо другое значение, кроме 
        EN или RU вызывает исключение AttributeError.
    """
    def __init__(self, language="EN") -> None:
        """инициализация класса"""
        self._language = language

    def change_lang(self) -> str:
        """метод меняет раскладку клавиатур EN на RU
        и наоборот. Возвращает текущее значение раскладки."""
        if self._language == "EN":
            self._language = "RU"
            return self._language
        elif self._language == "RU":
            self._language = "EN"
            return self._language

    @property
    def language(self) -> str:
        """Метод-геттер. Позволяет получить значение _language."""
        return self._language

    @language.setter
    def language(self, language: str) -> None | Exception:
        """Метод-сеттер. Не устанавливает новое значение, а 
        выбрасывает исключение, если language не RU и не EN."""
        if (language != 'RU') or (language != 'EN'):
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Goods, Mixin):
    """Класс KeyBoard- наследник класса Goods и миксина Mixin.
    Добавлен атрибут _language: str- принимающий значения EN или RU.
    Любое другое значение вызывает исключение. Для него определены 
    геттер и сеттер.
    Атрибуты, унаследованные от Goods:
    -__name:str - имя, приватный атрибут,
    -price: float - цена,
    -quantity: int - количество
    Атрибуты, унаследованные от Mixin:
    - _language: str- принимает значения EN или RU

    Методы:
    - __init__  - инициализация класса

    Методы, унаследованные от Mixin:
    - change_lang- метод меняет раскладку клавиатур EN на RU
        и наоборот. Возвращает текущее значение раскладки.
        Попытка установить какое-либо другое значение, кроме 
        EN или RU вызывает исключение AttributeError.
    """
    def __init__(self, name="", price=0.0, quantity=0, language="EN") -> None:
        """инициализация класса"""
        super().__init__(name, price, quantity)
        self._language = language
