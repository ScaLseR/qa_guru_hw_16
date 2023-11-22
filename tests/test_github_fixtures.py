"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selene import have, browser


@pytest.fixture(params=[(1920, 1080), (2880, 1620)])
def browser_desktop_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(params=[(828, 1792), (750, 1334)])
def browser_mobile_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_desktop(browser_desktop_size):
    browser.open('https://github.com')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_mobile_size):
    browser.open('https://github.com')

    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))