import pytest

from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


# @pytest.mark.skip()
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,
                    MainPageLocators.LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


# @pytest.mark.skip()
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, MainPageLocators.LINK)
    page.open()
    page.should_be_login_page()
