import allure
import requests
import data

class TestGetOrder:

    @allure.description('Тест получения полного списка заказов')
    def test_get_orders(self):
        order_list = requests.get(data.URL_DO_ORDER)

        assert order_list.status_code == 200, f"Ожидаемый статус код 200, но получен {order_list.status_code}."
        assert type(order_list.json()) == dict, "Ответ должен быть списком."
        assert 'orders' in order_list.json(), "Ответ должен содержать поле 'id'."
