import allure

from workingnomads_autotests_web.model.application import app


@allure.tag("web")
@allure.feature(f'Bookmark')
@allure.story("First filter out jobs and add one of them to bookmarks")
def test_bookmark_job(login):
    with allure.step('Filter jobs by category, position type and key words'):
        app.main_page.verify_main_page() \
            .enter_key_words()\
            .filter_by_category()\
            .filter_by_position_type()
    with allure.step('Bookmark second one in provided results'):
        app.main_page.save_job_as_a_bookmark()
    with allure.step('Go to Jobs Bookmark page and verify expected result'):
        app.bookmarks_page.open()\
            .verify_one_job_added()

