from pages.login_page import LoginPage

def test_successful_purchase(driver, base_url):
    # Реализация цепочки вызовов (Method Chaining)
    complete_message = (
        LoginPage(driver, base_url)
        .open()
        .login("standard_user", "secret_sauce")
        .add_first_item_to_cart()
        .go_to_cart()
        .click_checkout()
        .fill_checkout_info("Ivan", "Ivanov", "12345")
        .click_continue()
        .click_finish()
        .get_complete_message()
    )
    
    assert "Thank you for your order!" in complete_message