class InstantiateCSVError(Exception):
    """Класс InstantiateCSVError для обработки исключения, возникающего
    при открытии csv-файла в случае, если в нем отсутствуют какие-либо
    необходимые столбцы.
    Атрибуты:
    -message:str - сообщение об ошибке

    Методы:
    -__init__-инициализация класса
    -__str__- возвращает строку для печати с сообщением об ошибке
    """
    def __init__(self, message=""):
        if message:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        """возвращает тип ошибки и сообщение"""
        return "InstantiateCSVError: " + str(self.message)
      
