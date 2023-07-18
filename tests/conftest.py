import os
from urllib import request

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app

from workingnomads_autotests_web.utils import attach
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_adoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1200
    browser.config.window_height = 800
    browser.config.base_url = 'https://www.workingnomads.com'
    browser.config.timeout = 2.0

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="session")
def login():
    app.user_log_in.open() \
        .fill_email(user.email) \
        .fill_password(user.password) \
        .login_button()
    return app
