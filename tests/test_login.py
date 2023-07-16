import allure

from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app


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


@allure.tag("web")
@allure.feature(f'Sign in with invalid data')
@allure.story("Checking if an error is displayed when entering a password that is not in the system")
def test_unsuccessful_login():
    with allure.step('Select login and enter an invalid password'):
        app.user_log_in.open() \
            .fill_email(user.email) \
            .fill_password(user.invalid_password) \
            .login_button()
    with allure.step('Check for an expected error'):
        app.user_log_in.check_expected_error_message()


@allure.tag("web")
@allure.feature(f'Edit account')
@allure.story("Go to account page and fill first and last names of your account")
def test_edit_account():
    with allure.step('Open account page and enter data'):
        app.account_setting.open_account_setting() \
            .enter_first_name(user.first_name) \
            .enter_last_name(user.last_name) \
            .update_button()
    with allure.step('Check that account details changed'):
        app.account_setting.check_for_successful_update()


@allure.tag("web")
@allure.feature(f'Delete account')
@allure.story("Delete account and verify it")
def test_delete_account():
    with allure.step('Open delete account option from account page and click the delete button'):
        app.account_setting.open_delete_account()\
            .choose_delete_account()
    with allure.step('Verify that account deleted'):
        app.account_setting.account_deleted_check()
