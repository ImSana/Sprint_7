import allure
from creat_curier import *

class TestGetOrdersList:

    @allure.description("Получаем список заказов")
    @allure.title('Успешное получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(TestAPIOrdersLinks.main_url + TestAPIOrdersLinks.main_orders_url)
        orders_list = response.json()["orders"]
        assert response.status_code == 200 and isinstance(orders_list, list) == True

    @allure.description("Ошибка при получении списка заказов")
    @allure.title('Ошибка "Курьер не найден" при получении списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(TestAPIOrdersLinks.main_url + TestAPIOrdersLinks.main_orders_url)
        orders_list = response.json()["orders"]
        assert response.status_code == 200 and isinstance(orders_list, list) == True
