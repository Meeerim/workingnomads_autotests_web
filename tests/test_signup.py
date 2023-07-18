import allure
from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app


@allure.tag("web")
@allure.feature(f'Signing up with invalid credentials')
@allure.story("Verify that an appropriate error message is displayed and still on same url")
def test_with_invalid_email():
    with allure.step('Sign up with registered email address'):
        app.user_sign_up.open(). \
            fill_email(user.email) \
            .fill_password(user.password) \
            .reenter_password(user.password) \
            .agree_with_terms() \
            .agree_with_policy() \
            .sign_up_button()
    with allure.step('Verify for an expected error and page url is the same'):
        app.user_sign_up.email_error_message_displayed()\
            .verify_sign_up_page()



@allure.tag("web")
@allure.feature(f'Signing up  with invalid credentials')
@allure.story("Verify that an appropriate error message is displayed and still on same url")
def test_with_invalid_password():
    with allure.step('Sign up with easy and common password'):
        app.user_sign_up.open(). \
            fill_email(user.email) \
            .fill_password(user.wrong_password) \
            .reenter_password(user.wrong_password) \
            .agree_with_terms() \
            .agree_with_policy() \
            .sign_up_button()
    with allure.step('Verify for an expected error and page url is the same'):
        app.user_sign_up.password_error_message_displayed()\
            .verify_sign_up_page()