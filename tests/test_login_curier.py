import pytest
import allure
from ready_data import TestCourier, CourierErrors
from courier_api import *
from urls import TestAPICourierLinks


class TestCourierLoginAPI:
    @allure.description('Проверка входа с корректными данными')
    @allure.title('Успешный вход по ручке логина')
    def test_courier_login_success(self, test_user):
        login_courier = {"login": test_user[1][0],
                        "password": test_user[1][1]}
        r = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 200 and r.json()['id'] > 0

    @allure.description('Проверка входа с некорректными данными')
    @allure.title('Вход без пароля')
    def test_courier_login_no_such_user_fail(self, test_user):
        login_courier = {"login": test_user[1][1],
                        "password": test_user[1][0]}
        r = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 404 and r.json()['message'] == CourierErrors.login_no_such_user

    @allure.description('Проверка входа с отправкой недостаточных данных')
    @allure.title('Вход с недостаточными данными')
    @pytest.mark.parametrize('user_data', (TestCourier.login_empty_login, TestCourier.login_empty_password, TestCourier.login_only_password))
    def test_courier_login_no_data_fail(self, user_data):
        r = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.login_no_data