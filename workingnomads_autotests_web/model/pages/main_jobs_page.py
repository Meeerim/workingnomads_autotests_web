from selene import browser, have, be, command


class MainJobsPage:
    def verify_main_page(self):
        browser.should(have.url_containing('/jobs'))
        return self

    def is_login_successful(self):
        browser.element('.alert').should(have.text('Successfully signed in.'))
        return self

    def filter_by_category(self):
        browser.element('.side-menu-categories.search-bar__action').click()
        browser.all('.ng-binding').element_by(have.exact_text('Human Resources')).click()
        return self

    def enter_key_words(self):
        browser.all('.ng-binding').element_by(have.text('recruiting')).click().perform(command.js.scroll_into_view)
        return self

    def filter_by_position_type(self):
        browser.element('.side-menu-positionTyoes').click()
        browser.all('.ng-binding').element_by(have.text('Full-time')).click()
        return self

    def save_job_as_a_bookmark(self):
        browser.element('#job-47447 i.fa.fa-star').click()
        return self


