
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT_NAME  = (By.CSS_SELECTOR,".product_main > h1")
    BUSKET_PRODUCT_NAME  = (By.CSS_SELECTOR,".alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main > .price_color")
    BUSKET_PRODUCT_PRICE  = (By.CSS_SELECTOR,".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1)")
