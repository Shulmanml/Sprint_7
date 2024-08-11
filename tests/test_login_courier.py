import requests
import data
import helpers
import allure

class TestLoginCourier:

    @classmethod
    def setup_class(cls):
        cls.courier = helpers.register_new_courier_and_return_login_password()

    #@allure.description('Тест успешной авторизации')
    def test_login_courier_success(self):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1]
        }
        response = requests.post(data.URL_LOGIN_COURIER, json = payload)

        assert response.status_code == 200, f"Ожидаемый ответ 200, но получен {response.status_code}."
        assert 'id' in response.json(), "Ответ должен содержать поле 'id'."

    @allure.description('Тест на получение кода ошибки при попытке авторизации без отправки обязательного поля "password"')
    def test_login_without_password(self):
        payload = {
            "login": self.courier[0],
            "password": ""
        }
        response = requests.post(data.URL_LOGIN_COURIER, json = payload)

        assert response.status_code == 400, f"Ожидаемый ответ 400, но получен {response.status_code}."
        assert response.json() == {"code": 400,
                                   "message":  "Недостаточно данных для входа"}, f"Ожидаемый ответ {"code":400,'message':'Недостаточно данных для входа'} но получен {response.json()}."

    @allure.description('Тест на получение кода ошибки при попытке авторизации с несуществущим login')
    def test_login_with_not_exist_login(self):
        payload = {
            "login": data.LOGIN,
            "password": self.courier[1]
        }
        response = requests.post(data.URL_LOGIN_COURIER, json = payload)

        assert response.status_code == 404, f"Ожидаемый ответ 400, но получен {response.status_code}."
        assert response.json() == {"code": 404,
                                   "message": "Учетная запись не найдена"}, f"Ожидаемый ответ {"code":404,'message':'Учетная запись не найдена'} но получен {response.json()}."


    @classmethod
    def teardown_class(cls):
        courier_id = helpers.get_id_after_login_with_new_courier()
        delete_courier = requests.delete(f'{data.URL_DELETE_COURIER}{courier_id}')

        assert delete_courier.status_code == 200, "не найден id курьера"


