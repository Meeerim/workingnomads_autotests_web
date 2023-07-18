from selene import browser, have, be


class LogInPage:
    def open(self):
        browser.open('/users/sign_in')
        return self

    def fill_email(self, email):
        browser.element('[name=login]').type(email)
        return self

    def fill_password(self, password):
        browser.element('[name=password]').type(password)
        return self

    def login_button(self):
        browser.element('[name=commit]').click()
        return self

    def check_expected_error_message(self):
        browser.element('.alert').should(have.text('The e-mail address and/or password you specified are '
                                                                'not correct.'))
        return self
