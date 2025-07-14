import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.public_http_buider import get_public_http_client
from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/login
    """

    @allure.step("Authenticate user")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с username и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        request_data = request.model_dump(by_alias=True)
        print("Sending login request with data:", request_data)  # Логирование
        return self.post(
            f"{APIRoutes.AUTHENTICATION}",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)

        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
