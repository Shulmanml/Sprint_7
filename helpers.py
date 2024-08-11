import requests
import random
import string
import data

def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(data.URL_CREATE_COURIER, json=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def get_id_after_login_with_new_courier():
    courier_id = None
    new_courier = register_new_courier_and_return_login_password()
    response = requests.post(data.URL_LOGIN_COURIER, json={
        "login": new_courier[0],
        "password": new_courier[1]
    })
    if response.status_code == 200:
        courier_id = response.json()['id']
    return courier_id

def generate_random_login(length):
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for i in range(length))
    return login

def generate_random_password(length):
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(length))
    return password

def generate_random_name(length):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name
