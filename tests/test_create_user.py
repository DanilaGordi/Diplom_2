import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage


@allure.feature('Проверяем создание пользователя')
class TestApiCreateUser:
    @allure.title('Тест создания нового пользователя')
    def test_create_new_user_successful(self, registered_user):
        response = registered_user
        assert response.status_code == 200 and response.json()['success']

    @allure.title('тест создания дубликата пользователя')
    def test_create_duplicate_user_error(self, user_data):
        payload = user_data
        response = requests.post(EndpointsUrl.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessage.EXIST_USER

    @allure.title('Тест ошибки при создании пользователя без обязательного параметра')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_no_required_field_error(self, field):
        payload = helpers.payload
        del payload[field]
        response = requests.post(EndpointsUrl.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessage.REQUIRED_FIELD
