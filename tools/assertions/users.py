from typing import List

import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema, GetUsersResponseSchema
from tools.assertions.base import assert_equal
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
        get_users_response: List[str]

):
    """
    Проверяет, что ответ на получение пользователей соответствует нужному формату и их действительно 100.

    :param get_users_response: Ответ API при запросе данных пользователя.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    logger.info("Check get users response")

    assert len(get_users_response) == 100, (
        f"Expected 100 emails, got {len(get_users_response)}"
    )

    for user in get_users_response:
        # Для обычных email
        if "@" in user:
            assert "." in user.split("@")[1], f"Invalid email format: {user}"
        # Для специальных идентификаторов (Unhuman...)
        elif user.startswith("Unhuman"):
            assert len(user) > 20, f"Invalid Unhuman ID format: {user}"
        # Для других форматов (string55551 и т.д.)
        else:
            assert len(user) >= 5, f"Invalid identifier format: {user}"
