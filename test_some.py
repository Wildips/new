import pytest
from selene import be, have

DESTINATION_URL: str = 'https://google.com'


def test_first(customized_browser):
    # ARRANGE
    customized_browser.open(DESTINATION_URL)
    # ACTION
    customized_browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    # ASSERT
    assert customized_browser.element('[id="search"]').should(
        have.text('User-oriented Web UI browser tests')), "Text doesn't found"


@pytest.mark.parametrize(
    "element_selector,awaiting_text",
    [('[id="result-stats"]', 'Результатов: примерно 0'),
     ('[class="card-section"]', 'По запросу sdfsdfdsfdsfdfkigjoisfjgsf ничего не найдено.')])
def test_second(customized_browser, element_selector, awaiting_text):
    # ARRANGE
    customized_browser.open(DESTINATION_URL)
    # ACTION
    customized_browser.element('[name="q"]').should(be.blank).type('sdfsdfdsfdsfdfkigjoisfjgsf').press_enter()
    # ASSERT
    assert customized_browser.element(element_selector).should(
        have.text(awaiting_text)), "Text doesn't found"

# conflict for changes
