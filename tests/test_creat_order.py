import pytest
import allure
from ready_data import OrdersErrors
from courier_api import *
from tests.conftest import courier_password, courier_login
from urls import TestAPIOrdersLinks, TestAPICourierLinks


class TestCreateOrder:

    @allure.description('Создание заказа с разными вариантами цветов')
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_order_creation_with_different_colors_success(self, color):
        TestOrder.test_order["color"] = [color]
        payload = json.dumps(TestOrder.test_order)
        response = requests.post(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.main_orders_url, data=payload)
        assert response.status_code == 201 and 'track' in response.text


class TestTrackOrder:
    @allure.description('Успешное получение данных о заказе')
    @allure.title('Получение данных о заказе')
    def test_order_track_success(self):
        new_track = return_new_order()
        payload = {"t": new_track}
        response = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track), data=payload)
        assert response.status_code == 200 and 'order' in response.text

    @allure.description('Получение данных о заказе без номера заказа')
    @allure.title('Получение данных о заказе без номера')
    def test_order_track_no_order_id_fail(self):
        new_track = return_new_order()
        payload = {"t": new_track}
        response = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url, data=payload)

        assert response.status_code == 400 and response.json()['message'] == OrdersErrors.track_order_no_data

    @allure.description('Получение данных о заказе с несуществующим номером')
    @allure.title('Получение данных о несуществующем заказе')
    def test_order_track_wrong_order_id_fail(self):
        new_track = 0
        payload = {"t": new_track}
        response = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track), data=payload)
        assert response.status_code == 404 and response.json()['message'] == OrdersErrors.track_order_no_such_order


class TestAcceptOrder:

    @allure.description('Успешное принятие заказа')
    @allure.title('Прием заказа курьером')
    def test_order_accept_success(self, courier_login, courier_password):
        new_courier = {"login": courier_login,
                        "password": courier_password}

        courier_signin = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=new_courier)
        courier_id = courier_signin.json()['id']

        new_track = return_new_order()
        track_order = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track))
        order_id = track_order.json()['order']['id']

        payload = {"id": order_id,
                   "courierId": courier_id}
        response = requests.put(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.accept_order_url + str(order_id) + '?courierId=' + str(courier_id), data=payload)

        assert response.status_code == 200 and response.json()['ok'] == True

    @allure.description('Принятие заказа при отправке данных без id курьера')
    @allure.title('Прием заказа без id курьера')
    def test_order_accept_no_сourier_id_fail(self, courier_login, courier_password):
        new_courier = {"login": courier_login,
                        "password": courier_password}
        courier_signin = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=new_courier)
        courier_id = courier_signin.json()['id']

        new_track = return_new_order()
        track_order = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track))
        order_id = track_order.json()['order']['id']

        payload = {"id": order_id,
                   "courierId": courier_id}
        response = requests.put(
            TestAPIBaseLinks.main_url + TestAPIOrdersLinks.accept_order_url + str(order_id), data=payload)

        assert response.status_code == 400 and response.json()['message'] == OrdersErrors.accept_order_no_data

    @allure.description('Принятие заказа при отправке данных без id заказа')
    @allure.title('Прием заказа без id заказа')
    def test_order_accept_no_order_id_fail(self, courier_login, courier_password):
        new_courier = {"login": courier_login,
                        "password": courier_password}
        courier_signin = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=new_courier)
        courier_id = courier_signin.json()['id']

        new_track = return_new_order()
        track_order = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track))
        order_id = track_order.json()['order']['id']

        payload = {"id": order_id,
                       "courierId": courier_id}
        response = requests.put(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.accept_order_url + 'courierId=' + str(courier_id), data=payload)

        assert response.status_code == 400 and response.json()['message'] == OrdersErrors.accept_order_no_order_number

    @allure.description('Принятие заказа с отправкой неверного id курьера')
    @allure.title('Прием заказа с некорректным id')
    def test_order_accept_wrong_courier_id_fail(self):
        courier_id = non_existing_id_courier()
        new_track = return_new_order()
        track_order = requests.get(TestAPIBaseLinks.main_url + TestAPIOrdersLinks.track_order_url + str(new_track))
        order_id = track_order.json()['order']['id']

        payload = {"id": order_id,
                   "courierId": courier_id}
        response = requests.put(
            TestAPIBaseLinks.main_url + TestAPIOrdersLinks.accept_order_url + str(order_id) + '?courierId=' + str(
                courier_id), data=payload)

        assert response.status_code == 404 and response.json()['message'] == OrdersErrors.accept_order_no_such_courier