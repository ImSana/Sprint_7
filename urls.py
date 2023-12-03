

class TestAPIBaseLinks:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    

class TestAPICourierLinks:
    login_url = '/api/v1/courier/login'
    courier_url = '/api/v1/courier/'

    courier_orders_url = '/ordersCount'


class TestAPIOrdersLinks:
    main_orders_url = '/api/v1/orders'
    accept_order_url = '/api/v1/orders/accept/'
    finish_order_url = '/api/v1/orders/finish/'
    cancel_order_url = '/api/v1/orders/cancel'
    track_order_url = '/api/v1/orders/track?t='
