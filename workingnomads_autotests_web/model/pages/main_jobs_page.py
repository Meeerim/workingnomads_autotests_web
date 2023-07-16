from selene import browser, have


class MainJobsPage:
    def verify_main_page(self):
        browser.open('/jobs')
        browser.should(have.url_containing('/jobs'))
        return self

    def is_login_successful(self):
        browser.element('.alert').should(have.text('Successfully signed in.'))
        return self

    def filter_by_category(self):
        browser.element('.search-bar__action__button select').click()
        browser.all('.category.key').element_by(have.exact_text('Human Resources')).click()
        return self

    def enter_key_words(self):
        browser.element('#q').type('recruit')
        browser.all('.ng-binding').element_by(have.text('recruiting')).click()
        browser.element('#q').type('hiring')
        browser.all('.ng-binding').element_by(have.text('hiring')).click()
        return self

    def filter_by_position_type(self):
        browser.element('.search-bar__action__label span').click()
        browser.all('.positionType.id').element_by(have.text('Full time')).click()
        return self

    def save_job_as_a_bookmark(self):
        browser.element('.fa fa-star').click()
        return self


