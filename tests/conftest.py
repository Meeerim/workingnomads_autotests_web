from selenium.common import NoSuchElementException

from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app

from workingnomads_autotests_web.utils import attach
import os
import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv



@pytest.fixture(scope="function")
def login():
    app.user_log_in.open() \
        .fill_email(user.email) \
        .fill_password(user.password) \
        .login_button()
    return app


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


DEFAULT_BROWSER_VERSION = "99.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='99.0'
    )




@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
    options.add_argument("--enable-automation")  # Enable automation to accept cookies automatically
    options.add_argument("--start-maximized")  # Start the browser in maximized mode
    options.add_argument("--no-sandbox")
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
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

    browser.config.timeout = 60
    browser.config.window_width = 1200
    browser.config.window_height = 800
    browser.config.base_url = 'https://www.workingnomads.com'

    load_dotenv()

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
