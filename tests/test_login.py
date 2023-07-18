import allure

from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app

@allure.tag("web")
@allure.feature(f'Login with invalid data')
@allure.story("Checking if an error is displayed when entering a password that is not in the system")
def test_unsuccessful_login():
    with allure.step('Select login and enter an invalid password'):
        app.user_log_in.open() \
            .fill_email(user.email) \
            .fill_password(user.wrong_password) \
            .login_button()
    with allure.step('Check for an expected error'):
        app.user_log_in.check_expected_error_message()


@allure.tag("web")
@allure.feature(f'Sign in')
@allure.story("Successful login and expected redirection of URL")
def test_successful_login():
    with allure.step('Select login and enter an valid username and password'):
        app.user_log_in.open() \
            .fill_email(user.email) \
            .fill_password(user.password) \
            .login_button()
    with allure.step('Successfully signed in and in the homepage'):
        app.main_page.verify_main_page()
        app.main_page.is_login_successful()






