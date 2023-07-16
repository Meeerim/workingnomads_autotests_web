from selene import browser, have


class AccountSettingPage:
    def open_account_setting(self):
        browser.open('/users/profile')
        return self

    def enter_first_name(self, first_name):
        browser.element('[name=first_name]').type(first_name)
        return self

    def enter_last_name (self, last_name):
        browser.element('[name=last_name]').type(last_name)
        return self

    def update_button(self):
        browser.element('.submit.btn.btn-primary').click()
        return self

    def check_for_successful_update(self):
        browser.element('').should(have.text(''))
        return self

    def open_delete_account(self):
        browser.open('/users/delete_account')
        return self

    def choose_delete_account(self):
        browser.element('#user-form').click()
        browser.element('.btn.btn-danger.btn-ok').click()
        return self

    def account_deleted_check(self):
        browser.element('.alert').should(have.text('Account deleted.'))
        return self

