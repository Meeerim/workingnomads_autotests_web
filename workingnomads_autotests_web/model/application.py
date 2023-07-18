

from workingnomads_autotests_web.model.pages.account_settings_page import AccountSettingPage
from workingnomads_autotests_web.model.pages.job_bookmarks_page import JobBookmarksPage
from workingnomads_autotests_web.model.pages.main_jobs_page import MainJobsPage
from workingnomads_autotests_web.model.pages.user_log_in_page import LogInPage
from selene import browser

from workingnomads_autotests_web.model.pages.user_sing_up_page import UserSignUpPage


class Application:
    def __init__(self):
        self.user_sign_up = UserSignUpPage()
        self.user_log_in = LogInPage()
        self.account_setting = AccountSettingPage()
        self.main_page = MainJobsPage()
        self.bookmarks_page = JobBookmarksPage()

    def open(self):
        browser.open('/')
        return self


app = Application()
