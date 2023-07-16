import pytest
from selene.support.shared import browser

from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app


@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 700
    browser.config.base_url = 'https://www.workingnomads.com'
    browser.config.timeout = 10.0

    yield

    browser.quit()


@pytest.fixture(scope="function",autouse=True)
def login():
    if not app.main_page.is_login_successful():
        app.user_log_in.open() \
            .fill_email(user.email) \
            .fill_password(user.password) \
            .login_button()
    assert app.main_page.is_login_successful(), "Failed to log in"
    return app

