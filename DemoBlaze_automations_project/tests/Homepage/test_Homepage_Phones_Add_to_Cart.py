from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.utils.Test_Base import TestBaseHomepage
from src.pages.Homepage_Item_Select import HomepageItems
from src.Locators.Product_Information import ProductLocators


class PhonesAddtoCart(TestBaseHomepage):

    def test_1_add_to_cart(self):
        HomepageItems(self.driver).nokia_lumina_click()
        add_to_cart_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ProductLocators().add_to_cart_button_selector)))
        add_to_cart_btn.click()
