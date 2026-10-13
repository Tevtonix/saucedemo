from pages.base_page import BasePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from selenium.webdriver.common.by import By

class CheckoutStepOnePage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        return (
            self.input_text(self.FIRST_NAME_INPUT, first_name)
            .input_text(self.LAST_NAME_INPUT, last_name)
            .input_text(self.POSTAL_CODE_INPUT, postal_code)
        )

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
        return CheckoutStepTwoPage(self.driver, self.driver.current_url)