import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.public_http_buider import get_public_http_client
from tools.routes import APIRoutes


class StatusCodesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Get Bad request")
    @tracker.track_coverage_httpx(f"{APIRoutes.STATUS_CODES}/bad-request")
    def get_bad_request_api(self) -> Response:
        """
        Метод получения Bad request.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.STATUS_CODES}/bad-request")


def get_status_codes_client() -> StatusCodesClient:
    """
    Функция создаёт экземпляр StatusCodesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию StatusCodesClient.
    """
    return StatusCodesClient(client=get_public_http_client())
