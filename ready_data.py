import datetime
from datetime import date as d


class CourierErrors:
    create_no_data = "Недостаточно данных для создания учетной записи"
    create_already_exist = "Этот логин уже используется. Попробуйте другой."

    login_no_data = "Недостаточно данных для входа"
    login_no_such_user = "Учетная запись не найдена"


class OrdersErrors:
    track_order_no_data = "Недостаточно данных для поиска"
    track_order_no_such_order = "Заказ не найден"

    accept_order_no_order_number = "Недостаточно данных для поиска"
    accept_order_no_such_courier = "Курьера с таким id не существует"
    accept_order_no_data = "Недостаточно данных для поиска"


class TestAPICourierLinks:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    login_url = '/api/v1/courier/login'
    courier_url = '/api/v1/courier/'

    courier_orders_url = '/ordersCount'


class TestAPIOrdersLinks:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    main_orders_url = '/api/v1/orders'
    accept_order_url = '/api/v1/orders/accept/'
    finish_order_url = '/api/v1/orders/finish/'
    cancel_order_url = '/api/v1/orders/cancel'
    track_order_url = '/api/v1/orders/track?t='


class TestCourier:
    login_only_password = {"password": "qwerty"}
    login_empty_password = {"login": "tester", "password": ""}
    login_empty_login = {"login": "", "password": "qwerty!"}

    create_no_login_courier = {"password": "qwerty", "firstName": 'ivan'}
    create_no_password_courier = {"login": "tester", "firstName": "ivan"}
    create_empty_login = {"login": "", "password": "qwerty", "firstName": "ivan"}
    create_empty_password = {"login": "tester", "password": "", "firstName": "ivan"}


class TestOrder:
    delivery_date = (d.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    test_order = {"order":
{
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
 }
    }

