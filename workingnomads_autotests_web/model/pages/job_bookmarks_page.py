from selene import browser, be


class JobBookmarksPage:
    def open(self):
        browser.element('/bookmarks')
        return self

    def verify_one_job_added(self):
        parent_element = browser.element('.ng-scope[ng-repeat="job in bookmarkedJobs"]')
        assert len(parent_element) == 1
        return self

