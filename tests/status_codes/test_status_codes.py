from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.status_codes.status_codes_client import get_status_codes_client
from clients.status_codes.status_codes_schema import StatusCodesSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.status_codes import assert_status_code_response


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.REGRESSION, AllureTag.GET_ENTITY)
@allure.epic(AllureEpic.ADMINISTRATION)
@allure.feature(AllureFeature.STATUS_CODES)
@allure.parent_suite(AllureEpic.ADMINISTRATION)
@allure.suite(AllureFeature.STATUS_CODES)
class TestStatusCodes:
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get bad request")
    @allure.severity(Severity.MINOR)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_bad_request(self):
        response = get_status_codes_client().get_bad_request_api()
        response_data = StatusCodesSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_status_code_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
