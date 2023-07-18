from selene import browser, be, have


class JobBookmarksPage:
    def open(self):
        browser.element('/bookmarks')
        return self

    def verify_one_job_added(self):
        browser.element('#job-47447').should(be.visible)
        return self
