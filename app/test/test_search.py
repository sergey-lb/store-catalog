from app.catalog.catalog import Catalog
from app.catalog.option import Option
from app.catalog.product import Product


def test_search():
    t_shirt = Product('Футболка J-Design, Стимпанк', 'Футболки')
    t_shirt.add_option(Option('Размер', '48'))
    t_shirt.add_option(Option('Цвет', 'Чёрный'))
    t_shirt.add_option(Option('Материал', 'хлопок'))

    bicycle = Product('Велосипед Mikado Blitz Evo 26', 'Велосипеды')
    bicycle.add_option(Option('Производитель', 'Stinger'))
    bicycle.add_option(Option('Модель', '26SHV.BLITZEVO.18BK8'))
    bicycle.add_option(Option('Тип', 'Горный'))
    bicycle.add_option(Option('Вид', 'Хардтейл'))
    bicycle.add_option(Option('Назначение', 'Универсальный'))
    bicycle.add_option(Option('Цвет', 'Черный'))
    bicycle.add_option(Option('Материал рамы', 'Сталь'))
    bicycle.add_option(Option('Размер рамы', '15"'))
    bicycle.add_option(Option('Диаметр колес', '26"'))
    bicycle.add_option(Option('Количество скоростей велосипеда', '18'))

    phone = Product('Мобильный телефон Digma LINX A105 2G black', 'Телефоны')
    phone.add_option(Option('Тип SIM-карты', 'SIM'))
    phone.add_option(Option('Количество поддерживаемых SIM-карт', '1'))
    phone.add_option(Option('Тип корпуса', 'Моноблок'))
    phone.add_option(Option('Цвет', 'Черный'))
    phone.add_option(Option('Фонарик', 'Есть'))
    phone.add_option(Option('Поддерживаемые стандарты сотовой связи', 'GSM 900/1800 МГц'))
    phone.add_option(Option('Диагональ дисплея, "', '1.44'))
    phone.add_option(Option('Разрешение', '98 x 68'))
    phone.add_option(Option('Размеры, мм', '107 x 45.4 x 15 мм'))

    catalog = Catalog()
    catalog.add_product(t_shirt)
    catalog.add_product(bicycle)
    catalog.add_product(phone)

    expected = [bicycle]
    result = catalog.search_by_name('Mikado Blitz')

    assert result == expected
