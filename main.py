from utils.goods import Goods


def main():
    item1 = Goods("Смартфон", 10000, 20)
    item2 = Goods("Ноутбук", 20000, 5)
    print(item1.calculate_amount())
    print(item2.calculate_amount())
    Goods.pay_rate = 0.8

    item1.apply_discount()

    print(item1.price)
    print(item2.price)
    print(Goods.all)




if __name__ == "__main__":
    main()
