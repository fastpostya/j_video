from utils.goods import Goods


class Mixin():
    """Класс Mixin для реализации атрибута __language
    и метода change_language для смены его значения.
    _language - защищенный атрибут (protected).
    Для него определен геттер.

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


class KeyBoard(Goods, Mixin):
    """Класс KeyBoard- наследник класса Goods и миксина Mixin.
    Добавлен атрибут _language: str- принимающий значения EN или RU.
    Любое другое значение вызывает исключение. Для него определен 
    геттер.
    Атрибуты, унаследованные от Goods:
    -__name:str - имя, приватный атрибут. Определены геттер и сеттер.
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
    - __repr__ - метод возвращает представление класса. 
        Выводит все атрибуты объекта
    - __str__ - метод возвращает текст для печати, содержащий значения 
        аттрибутов объектов класса KeyBoard
    """
    def __init__(self, name="", price=0.0, quantity=0, language="EN") -> None:
        """инициализация класса"""
        super().__init__("", price, quantity)
        self._language = language
        self.name = name

    @property
    def name(self) -> str:
        """Метод-геттер. Позволяет получить значение __name."""
        return self.__name


    @name.setter
    def name(self, name: str) -> None:
        """Метод-сеттер. Не  
        выбрасывает исключение, если длина больше 10 символов."""
        self.__name = name
        return self.name

    def __repr__(self) -> str:
        """ метод возвращает представление класса. 
        Выводит все атрибуты объекта"""
        text = "KeyBoard("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        """ метод возвращает текст для печати, содержащий значения 
        аттрибутов объектов класса KeyBoard"""
        return f"Клавиатура: {self.name}, цена: {self.price}, " + \
            f"количество: {self.quantity}"       
