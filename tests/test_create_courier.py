import allure
import requests
import data
import helpers

class TestCreateCourier:

    @classmethod
    def setup_class(cls):
         cls.courier = helpers.register_new_courier_and_return_login_password()

    @allure.description('Тест успешного создания курьера')
    def test_create_courier_success(self):
        payload = {
            "login": data.LOGIN,
            "password": data.PASSWORD,
            "firstName": data.NAME
        }
        response = requests.post(data.URL_CREATE_COURIER, json = payload)

        assert response.status_code == 201, f"Ожидаемый ответ 201, но получен {response.status_code}."
        assert response.json() == {"ok": True}, f"Ожидаемый ответ {'ok': True} но получен {response.json()}."

    @allure.description('Тест на получение кода ошибки 400, при создании курьера без обязательного поля "password"')
    def test_create_courier_without_required_field_password(self):
        payload = {
            "login": data.LOGIN,
            "password": "",
            "firstName": data.NAME
        }
        response = requests.post(data.URL_CREATE_COURIER, json = payload)

        assert response.status_code == 400, f"Ожидаемый ответ 400, но получен {response.status_code}."
        assert response.json() == {"code":400,"message":"Недостаточно данных для создания учетной записи"}, f"Ожидаемый ответ {"code":400,'message':'Недостаточно данных для создания учетной записи'} но получен {response.json()}."

    @allure.description('Тест на получение кода ошибки 409, при создании курьера с существующим "login"')
    def test_create_two_couriers_with_same_login(self):
        payload = {
            "login": self.courier[0],
            "password": data.PASSWORD,
            "firstName": data.NAME
        }
        response = requests.post(data.URL_CREATE_COURIER, json = payload)

        assert response.status_code == 409, f"Ожидаемый ответ 409, но получен {response.status_code}."
        assert response.json() == {"code":409,"message":"Этот логин уже используется. Попробуйте другой."}, f"Ожидаемый ответ {'code':409,'message':'Этот логин уже используется. Попробуйте другой.'} но получен {response.json()}."


    @classmethod
    def teardown_class(cls):
        courier_id = helpers.get_id_after_login_with_new_courier()
        delete_courier = requests.delete(f'{data.URL_DELETE_COURIER}{courier_id}')

        assert delete_courier.status_code == 200, "не найден id курьера"








