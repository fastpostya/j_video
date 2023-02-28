import csv


class Goods():
    pay_rate = 1.0
    all = []

    def __init__(self, name="", price=0.0, quantity=0):
        """ инициализация экземпляра класса Goods. Праметры:
        -__name:str - имя, приватный атрибут,
        -price: float - цена,
        -quantity: int - количество"""
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        if len(str(self._Goods__name)) > 10:
            raise NameError("Длина названия товара не должна превышать 10 \
символов!", self._Goods__name)

    def __repr__(self) -> str:
        """ метод возвращает представление класса. 
        Выводит все атрибуты объекта"""
        text = "Goods("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        """ метод возвращает текст для печати, содержащий значения 
        аттрибутов объектов класса Channel"""
        return f"Товар: {self.__name}, цена: {self.price}, количество: {self.quantity}"       

    def calculate_amount(self):
        """метод возвращает общую стоимость всех товаров в экземпляре 
        класса Goods, расчитанных исходя из их цены price 
        и количества quantity"""
        return self.price * self.quantity

    def apply_discount(self):
        """метод возвращает цену, рассчитанную с учетом 
        уровня скидки pay_rate"""
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def load_from_csv(cls, path) -> list:
        """Метод загружает данные из файла csv, путь к которому 
        передан в параметре path и создает объекты класса Goods 
        в соответствии с данными из файла. Первая строка 
        в файле - заголовки. Возвращает список экземпляров класса 
        Goods.
        Параметры:
        -path- путь к файлу."""
        with open(path, "r", newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            goods_list = []
            for row in csv_data:
                name = row['name']
                price = int(row['price']) if float(row['price']).is_integer \
                else float(row['price'])
                quantity = int(row['quantity']) if \
                float(row['quantity']).is_integer else float(row['quantity'])
                goods_list.append(cls(name, price, quantity))
            return goods_list

    @staticmethod
    def is_integer(number) -> bool:
        """метод возвращает True- если переданное число number 
        имеет тип int, иначе - False"""
        return ((type(number) == int) or (type(number) == float)) \
            and (round(number) == number)


class Phone(Goods):
    def __init__(self, name="", price=0.0, quantity=0, number_of_sim=1):
        Goods.__init__(self, name, price, quantity)
        self._number_of_sim = number_of_sim
        self.name = name
        if number_of_sim == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


    @staticmethod
    def add_item(data1, data2):
        """ метод возвращает суммарное количество товара для
        объектов классов Phone и Goods. Для других объектов
        выбрасывает исключение"""
        if (isinstance(data1, Phone) or isinstance(data1, Goods)) and \
            (isinstance(data2, Phone) or isinstance(data2, Goods)):
            return data1.quantity + data2.quantity
        else:
            raise (ValueError, "Объекты должны быть типа Phone или Goods")

    def __repr__(self) -> str:
        """ метод возвращает представление класса. 
        Выводит все атрибуты объекта"""
        text = "Phone("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        """ метод возвращает текст для печати, содержащий значения 
        аттрибутов объектов класса Channel"""
        return f"Телефон: {self.name}, цена: {self.price}, \
количество: {self.quantity}, количество сим-карт: {self._number_of_sim}"

    @property
    def number_of_sim(self):
        """Метод-геттер. Позволяет плучить значение _number_of_sim."""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        """Метод-сеттер. Выбрасывает исключение, если number_of_sim меньше либо равно нулю и не целое."""
        if isinstance(number, int) and number > 0:
            self._number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
