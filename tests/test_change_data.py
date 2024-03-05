import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage

@allure.feature('Проверяем изменения данных пользователя')
class TestApiUpdateUserData:
    @allure.title('Тест изменения данных авторизованного пользователя')
    def test_auth_user_update_successful(self, user_token):
        token = user_token
        payload = helpers.payload
        response = requests.patch(EndpointsUrl.DELETE_USER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест изменения данных неавторизованного пользователя')
    def test_not_authorized_error(self):
        payload = helpers.payload
        response = requests.patch(EndpointsUrl.DELETE_USER, data=payload)
        assert response.status_code == 401
        assert ErrorMessage.NOT_AUTHORIZED in response.text
