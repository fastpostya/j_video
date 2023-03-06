from utils.goods import Goods, Phone
from utils.keyboard import KeyBoard
from utils.config import path_csv


def main():
    # try:
    #     item1 = Goods("Смартфон_123456789", 10000, 20)
    #     print(item1.calculate_amount())
    # except NameError:
    #     print("Ошибка. Длина названия товара не должна превышать 10 символов.")
    # item2 = Goods("Ноутбук", 20000, 5)  
    # print(item2.calculate_amount())
    # Goods.pay_rate = 0.8
    # try:
    #     print(repr(item2.load_from_csv(path_csv)) )
    #     for i in item2.all:
    #         print(i)
    # except FileNotFoundError:
    #     print(f"\nФайл {path_csv} не найден\n")
    # print(item2.price)
    # print(Goods.all)
    # item2.__name = "СуперСмартфон"

    # Задание 4
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    # phone1 = Phone("iPhone 14", 120_000, 5, 1)
    # print(phone1)
    # print(repr(phone1))
    # print(phone1.number_of_sim)
    # try:
    #     phone1.number_of_sim = 0
    # except Exception as text:
    #     print(text)
    # try:
    #     phone3 = Phone("gPhone 2", 5_000, 5, 0)
    # except Exception as text:
    #     print(text)
    # phone2 = Phone("mPhone 22", 30_000, 2, 1)
    # print(phone1.add_item(phone1, phone2))

    # Задание 5
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    # kb = KeyBoard('Dark', 9600, 5)
    print(kb)
    print(kb.language)
    kb.change_lang()
    print(kb.language)
    try:
        kb.language = 'CH'
    except AttributeError as error:
        print(error)


if __name__ == "__main__":
    main()
