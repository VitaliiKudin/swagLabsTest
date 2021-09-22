class BaseHelpers:
    """Store base helpers for webtesting"""

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, by, locator, value):
        """Find required element using by.X model, clear input field and enter value"""
        field_value = self.driver.find_element(by=by, value=locator)
        field_value.clear()
        field_value.send_keys(value)

    def clear_fields(self, by, locator):
        clear_element = self.driver.find_element(by=by, value=locator)
        clear_element.clear()

    def click_button(self, by, locator):
        click_on = self.driver.find_element(by=by, value=locator)
        click_on.click()

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains functions by text"""
        return self.driver.find_element_by_xpath(".//{element_tag}[contains(text(), {text})]")
