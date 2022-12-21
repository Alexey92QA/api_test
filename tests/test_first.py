import allure
from apod_1_step.api import start_url
from tests import credentials, creating_date
from schemas.apod import valid_schema

URL = credentials.base_url


class TestClass:
    @allure.title("Позитивный тест с корректными данными")
    @allure.description("""Авторизуемся и отправляем текущую дату""")
    def test_positive(self):
        params = {'api_key': credentials.auth, 'date': creating_date.now_date}
        response = start_url(url=URL).create_url(param=params, schema=valid_schema)
        with allure.step(f"Запрос отправлен, смотрим код ответа - {response.status_code}"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    @allure.title("Негативный тест с датой вне диапазона")
    @allure.description("""Авторизуемся и отправляем старую дату""")
    def test_negative(self):
        params_dict = {'api_key': credentials.auth, 'date': creating_date.stop_date}
        response = start_url(url=URL).create_url(param=params_dict, schema=valid_schema)
        with allure.step(f"Запрос отправлен, смотрим код ответа {response.status_code}"):
            assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
        with allure.step(f"Запрос отправлен, посмотрим текст ошибки {response.json().get('msg')}"):
            f"Текст ошибки - {response.status_code}"
            assert response.json().get(
                'msg') == 'Date must be between Jun 16, 1995 and ' + creating_date.error_date, f"Неверный текст " \
                                                                                               f"ошибки ответа, " \
                                                                                               f"получено " \
                                                                                               f"{response.json().get('msg')} "
