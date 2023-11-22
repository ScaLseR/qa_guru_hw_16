"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser


@pytest.fixture(params=[(1920, 1080, 'desktop'),
                        (2880, 1620, 'desktop'),
                        (828, 1792, 'mobile'),
                        (750, 1334, 'mobile')])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    if request.param[2] == 'desktop':
        return True
    else:
        return False


def test_github_desktop(browser_size):
    if not browser_size:
        pytest.skip(reason='browser for mobile size')

    browser.open('https://github.com')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    if browser_size:
        pytest.skip(reason='browser for desktop size')

    browser.open('https://github.com')

    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))
