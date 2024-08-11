import allure
import pytest
import requests
import data

class TestCreateOrder:
    @allure.description('Тест выбора цвета при заказе самоката')
    @pytest.mark.parametrize("colors, expected_status_code, expected_field_in_response",
        [
        (["BLACK"], 201, "track"),
        (["GREY"], 201, "track"),
        (["BLACK", "GREY"], 201, "track"),
        ([], 201, "track"),
        ])
    def test_create_order(self, colors, expected_status_code, expected_field_in_response):
        payload = {
        "firstName": data.FIRSTNAME,
        "lastName": data.LASTNAME,
        "address": data.ADDRESS,
        "metroStation": data.METROSTATION,
        "phone": data.PHONE,
        "rentTime": data.RENTTIME,
        "deliveryDate": data.DELIVERYDATE,
        "comment": data.COMMENT,
        "color": colors
    }
        response = requests.post(data.URL_DO_ORDER, json=payload)

        assert response.status_code == expected_status_code, f"Ожидаемый статус код {expected_status_code}, но получен {response.status_code}."
        assert expected_field_in_response in response.json(), f"Ответ должен содержать поле '{expected_field_in_response}'."

