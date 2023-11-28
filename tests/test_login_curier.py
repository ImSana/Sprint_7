import pytest
import allure
from static_data import TestCourier, CourierErrors
from creat_curier import *


class TestCourierLoginAPI:
    @allure.description('Проверяем попытку входа с отправкой существующих данных')
    @allure.title('Успешный вход по ручке логина')
    def test_courier_login_success(self, delete_user):
        login_courier = {"login": delete_user[1][0],
                        "password": delete_user[1][1]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 200 and r.json()['id'] > 0

    @allure.description('Проверяем попытку входа с отправкой несуществующих данных')
    @allure.title('Вход с несуществующим юзером')
    def test_courier_login_no_such_user_fail(self, delete_user):
        login_courier = {"login": delete_user[1][1],
                        "password": delete_user[1][0]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 404 and r.json()['message'] == CourierErrors.login_no_such_user

    @allure.description('Проверяем попытку входа с отправкой недостаточных данных')
    @allure.title('Вход с недостаточными данными')
    @pytest.mark.parametrize('user_data', (TestCourier.login_empty_login, TestCourier.login_empty_password, TestCourier.login_only_password, TestCourier.login_only_login))
    def test_courier_login_no_data_fail(self, user_data):
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.login_no_data
