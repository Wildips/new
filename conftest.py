import pytest as pytest
from selene.support.shared import browser


@pytest.fixture()
def customized_browser():
    browser.open()
    browser.driver.maximize_window()
    # Пример указания конкретного размера окна
    # browser.config.window_width = 1920
    # browser.config.window_height = 1080
    yield browser
    browser.quit()
