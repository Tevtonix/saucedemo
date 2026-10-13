from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def click_finish(self):
        self.click(self.FINISH_BUTTON)
        return CheckoutCompletePage(self.driver, self.driver.current_url)