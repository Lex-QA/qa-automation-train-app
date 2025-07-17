import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema, GetUsersResponseSchema, UpdateUserPasswordResponseSchema
from tools.assertions.base import assert_equal
from tools.info import Info
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create user response")

    assert_equal(response.register_data.login, request.login, "login")
    assert_equal(response.register_data.password, request.password, "password")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что фактические данные пользователя соответствуют ожидаемым.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check user")

    assert_equal(actual.register_data.login, expected.register_data.login, "login")
    assert_equal(actual.register_data.password, expected.register_data.password, "pass")


@allure.step("Check get user response")
def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    logger.info("Check get user response")

    assert get_user_response.login == create_user_response.register_data.login
    assert get_user_response.password == create_user_response.register_data.password


@allure.step("Check get user response")
def assert_get_users_response(
        users_response: GetUsersResponseSchema,
        expected_count: int = 100
):
    """
    Проверяет список пользователей:
    1. Что это именно список
    2. Что количество элементов соответствует ожидаемому
    3. Проверяет формат каждого элемента

    :param users_response: Ответ API со списком пользователей
    :param expected_count: Ожидаемое количество пользователей
    """
    logger.info("Check get users response")

    # Проверка количества
    assert len(users_response.root) == expected_count, (
        f"Expected {expected_count} users, got {len(users_response.root)}"
    )


@allure.step("Check update user password")
def assert_update_user_password_response(
        response: UpdateUserPasswordResponseSchema,
        expected_status: str = Info.SUCCESS,
        expected_message: str = Info.SUCCESSFULLY_CHANGED
):
    """
    Проверяет ответ на обновление пароля

    :param response: Ответ API
    :param expected_status: Ожидаемый статус
    :param expected_message: Ожидаемое сообщение
    """
    logger.info("Check update user password response")

    assert response.info.status == expected_status, (
        f"Expected status '{expected_status}', got '{response.info.status}'"
    )

    assert expected_message in response.info.message, (
        f"Expected message containing '{expected_message}', got '{response.info.message}'"
    )
