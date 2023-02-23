import csv


class Goods():
    pay_rate = 1.0
    all = []

    def __init__(self, __name="", price=0.0, quantity=0):
        """ инициализация экземпляра класса Goods. Праметры:
        -__name:str - имя, приватный атрибут,
        -price: float - цена,
        -quantity: int - количество"""
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        if len(__name) > 10:
            raise NameError("Длина названия товара не должна превышать 10 символов!")

    def __repr__(self) -> str:
        """ метод возвращает представление класса. Выводит все атрибуты объекта"""
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"Goods({text[:-2]})"

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
        """метод возвращает цену, рассчитанную с учетом уровня скидки pay_rate"""
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
                goods_list.append(cls(row['name'], int(row['price']), int(row['quantity'])))
            return goods_list

    @staticmethod
    def is_integer(number) -> bool:
        """метод возвращает True- если переданное число number 
        имеет тип int, иначе - False"""
        return ((type(number) == int) or (type(number) == float)) \
            and (round(number) == number)

