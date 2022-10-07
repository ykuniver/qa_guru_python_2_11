from selene.support.shared import browser
from selene import Element


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_date(self, year, month, day):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()
