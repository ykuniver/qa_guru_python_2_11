from selene import have
from selene.support.shared import browser


class DropDown:
    def __init__(self):
        pass

    @staticmethod
    def select(self, element, option):
        element.click()
        browser.all('[id^=react-select][id*=-option-]').by(
            have.exact_text(option)
        ).first.click()
