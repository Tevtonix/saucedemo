from pages.base_page import BasePage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def go_to_cart(self):
        self.click(self.CART_LINK)
        return CartPage(self.driver, self.driver.current_url)