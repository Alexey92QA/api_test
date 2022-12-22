import allure
from apod.api import start_url
import creating_date
import credentials
from schemas.apod import valid_schema

URL = 'https://api.nasa.gov'


class TestClass:
    @allure.title("Позитивный тест с корректными данными")
    @allure.description("""Авторизуемся и отправляем текущую дату""")
    def test_positive(self):
        params = {'api_key': credentials.auth, 'date': creating_date.now_date}
        response = start_url(url=URL).create_url(param=params, schema=valid_schema)
        with allure.step(f"Запрос отправлен, смотрим код ответа - {response.status}"):
            assert response.status == 200, f"Неверный код ответа, получен {response.status}"

    @allure.title("Негативный тест с датой вне диапазона")
    @allure.description("""Авторизуемся и отправляем старую дату""")
    def test_negative(self):
        params_dict = {'api_key': credentials.auth, 'date': creating_date.stop_date}
        response = start_url(url=URL).create_url(param=params_dict, schema=valid_schema)
        with allure.step(f"Запрос отправлен, смотрим код ответа {response.status}"):
            assert response.status == 400, f"Неверный код ответа, получен {response.status}"
        with allure.step(f"Запрос отправлен, посмотрим текст ошибки {response.response.get('msg')}"):
            f"Текст ошибки - {response.status}"
            assert response.response.get(
                'msg') == 'Date must be between Jun 16, 1995 and ' + creating_date.error_date, f"Неверный текст " \
                                                                                               f"ошибки ответа, " \
                                                                                               f"получено " \
                                                                                               f"{response.response.get('msg')} "
