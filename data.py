import helpers

URL_CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'

URL_DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/'

URL_LOGIN_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'

URL_DO_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'

LOGIN = helpers.generate_random_login(10)
PASSWORD = helpers.generate_random_password(10)
NAME = helpers.generate_random_name(10)
FIRSTNAME = 'Игорь'
LASTNAME = 'Вавилов'
ADDRESS = 'г Москва'
METROSTATION = 5
PHONE = 89053201212
RENTTIME = 4
DELIVERYDATE = '2024-08-20'
COMMENT = 'Привет'

