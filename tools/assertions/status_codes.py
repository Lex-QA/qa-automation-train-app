import allure

from clients.status_codes.status_codes_schema import StatusCodesSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger
from tools.status_codes import StatusCodes

logger = get_logger("STATUS_CODES_ASSERTIONS")


@allure.step("Check status code request body")
def assert_status_code_response(response: StatusCodesSchema):
    """
    Проверяет корректность ответа.

    :param response: Объект ответа.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    logger.info("Check bad request response")

    assert_equal(response.statusCode, 400, "400")
    assert_equal(response.description, StatusCodes.BAD_REQUEST, "Bad Request")
