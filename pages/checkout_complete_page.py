from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)