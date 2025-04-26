import random


def random_phone():
    """Генерация номера телефона"""

    random_phone = random.randint(10, 99)
    phone = f"799999999{random_phone}"
    return phone

def random_num():
    """Генерация рандомного значения для локатора"""

    random_num = random.randint(1, 10)
    return str(random_num)

def random_data():
    """Генерация рандомного значения для выбора даты"""

    random_data = random.randint(10, 20)
    data = f"0{random_data}"
    return str(data)


