from utils.goods import Goods
from utils.config import path_csv


def main():
    try:
        item1 = Goods("Смартфон_123456789", 10000, 20)
        print(item1.calculate_amount())
    except NameError:
        print("Ошибка. Длина названия товара не должна превышать 10 символов.")

    item2 = Goods("Ноутбук", 20000, 5)  
    print(item2.calculate_amount())
    Goods.pay_rate = 0.8
    try:
        print(repr(item2.load_from_csv(path_csv)) )
        for i in item2.all:
            print(i)
    except FileNotFoundError:
        print(f"\nФайл {path_csv} не найден\n")


    print(item2.price)
    print(Goods.all)
    item2.__name = "СуперСмартфон"


if __name__ == "__main__":
    main()
