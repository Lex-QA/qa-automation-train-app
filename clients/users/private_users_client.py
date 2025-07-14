import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """


    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}")
    def get_user_api(self) -> Response:
        """
         Метод получения пользователя по токен.

        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"{APIRoutes.USERS}")


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
