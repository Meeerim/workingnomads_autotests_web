import allure
from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app


@allure.tag("web")
@allure.feature(f'Sign up with valid data')
@allure.story("Verify that the user is successfully signed up and redirected to the expected page")
def test_successful_sign_in(open_browser):
    with allure.step('Sign up with new credentials'):
        app.user_sign_up.open(). \
            fill_email(user.email) \
            .fill_password(user.password) \
            .reenter_password(user.password) \
            .agree_with_terms() \
            .agree_with_policy() \
            .sign_up_button()
    with allure.step('Sign up '):
        app.user_sign_up.check_for_success_sign_up()


@allure.tag("web")
@allure.feature(f'Sign up  with invalid data')
@allure.story("Verify that an appropriate error message is displayed indicating invalid credential")
def test_unsuccessful_sign_up(open_browser):
    with allure.step('Sign up with credential that already registered'):
        app.user_sign_up.open(). \
            fill_email(user.email) \
            .fill_password(user.password) \
            .reenter_password(user.password) \
            .agree_with_terms() \
            .agree_with_policy() \
            .sign_up_button()
    with allure.step('Check for an expected error'):
        app.user_sign_up.check_for_error_message()
