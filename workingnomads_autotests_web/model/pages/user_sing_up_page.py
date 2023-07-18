from selene import browser, have, command


class UserSignUpPage:
    def open(self):
        browser.open('/users/sign_up')
        return self

    def fill_email(self, email):
        browser.element('[name=email]').perform(command.js.scroll_into_view).type(email)
        return self

    def fill_password(self, password):
        browser.element('[name=password1]').type(password)
        return self

    def reenter_password(self, password):
        browser.element('[name=password2]').type(password)
        return self

    def agree_with_terms(self):
        browser.element('label[for="id_tos"] '
                        'span').click()
        return self

    def agree_with_policy(self):
        browser.element('label[for="id_privacy"] span').click()
        return self

    def sign_up_button(self):
        browser.element('[name=commit]').click()
        return self

    def verify_sign_up_page(self):
        browser.should(have.url_containing('/users/sign_up'))
        return self

    def password_error_message_displayed(self):
        browser.element('.form-group.ion-locked p').should(have.text(' This password is too common.'))
        return self

    def email_error_message_displayed(self):
        browser.element('.form-group.ion-email p').should(have.text('A user is already registered with this '
                                                                    'e-mail address'))
        return self