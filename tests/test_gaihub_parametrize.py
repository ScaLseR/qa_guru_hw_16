"""
Переопределите параметр с помощью indirect параметризации на уровне теста
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


@pytest.mark.parametrize('browser_size', [(1920, 1080), (2880, 1620)], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_size', [(828, 1792), (750, 1334)], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com')

    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))
