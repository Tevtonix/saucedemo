import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    """Фикстура для ссылки"""
    return "https://www.saucedemo.com/"