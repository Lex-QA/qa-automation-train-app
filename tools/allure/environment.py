import os
import platform
import sys

from config import settings


def create_allure_environment_file():
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version

    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    items.extend([
        f'os_info={os_info}',
        f'python_version={python_version}'
    ])

    ci_pages_url = os.getenv("CI_PAGES_URL")
    if ci_pages_url:
        items.append(f'Coverage Report={ci_pages_url}/coverage.html')

    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
