from selene import have, command
from selene.support.shared import browser


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

    def reenter_password(self,password):
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

    def check_for_success_sign_up(self):
        browser.should(have.url_containing('/welcome'))
        browser.element('.title p').should(have.text('Thanks for opening an account with Working Nomads!'))
        return self

    def check_for_error_message(self):
        browser.should(have.url_containing('/users/sign_up'))
        browser.element('.form-group.ion-email p').should(have.text('A user is already registered with this '
                                                                          'e-mail address'))
        return self






