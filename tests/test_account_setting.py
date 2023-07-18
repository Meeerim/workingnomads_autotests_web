import allure

from workingnomads_autotests_web.data.users import user
from workingnomads_autotests_web.model.application import app


@allure.tag("web")
@allure.feature(f'Edit account')
@allure.story("Go to account page and fill first and last names of account")
def test_edit_account(login):
    with allure.step('Open account page and enter data'):
        app.account_setting.open_account_setting() \
            .enter_first_name(user.first_name) \
            .enter_last_name(user.last_name) \
            .update_button()
    with allure.step('Check that account details changed'):
        app.account_setting.check_for_successful_update()



