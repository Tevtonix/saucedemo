from pages.base_page import BasePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutStepOnePage(self.driver, self.driver.current_url)