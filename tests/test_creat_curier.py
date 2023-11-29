import pytest
import allure
from static_data import TestCourier, CourierErrors
from creat_curier import *


class TestCourierCreateAPI:
    @allure.description('Проверяем успешное создание курьера')
    @allure.title('Создание курьера с новыми данными')
    def test_courier_create_new_courier_success(self, test_user):
        user_data = test_user[0]

        assert user_data.status_code == 201 and user_data.json()['ok'] == True

    @allure.description('Проверяем создание курьера с использованием уже существующих данных')
    @allure.title('Создание курьера с повторными данными')
    def test_courier_create_already_existing_user_fail(self, test_user):
        exist_login_courier = \
            {
                "login": test_user[1][0],
                "password": test_user[1][1],
                "firstName": test_user[1][2]
            }

        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url, data=exist_login_courier)

        assert r.status_code == 409 and r.json()['message'] == CourierErrors.create_already_exist

    @allure.description('Проверяем создание курьера с недостаточным количеством обязательных данных')
    @allure.title('Создание курьера без обязательных данных')
    @pytest.mark.parametrize('user_data', (TestCourier.create_no_login_courier, TestCourier.create_no_password_courier,
                                           TestCourier.create_empty_login, TestCourier.create_empty_password))
    def test_courier_create_no_data_fail(self, user_data):
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.create_no_data

