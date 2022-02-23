
from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PSWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PSWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT = (By.CSS_SELECTOR, ".btn[name='registration_submit']")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT_NAME  = (By.CSS_SELECTOR,".product_main > h1")
    BUSKET_PRODUCT_NAME  = (By.CSS_SELECTOR,".alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main > .price_color")
    BUSKET_PRODUCT_PRICE  = (By.CSS_SELECTOR,".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1)")
    
class BasketPageLocators():    
    TOTAL_GOODS = (By.CSS_SELECTOR, "#basket_formset > .basket-items")
    TOTAL_GOODS_LABEL = (By.CSS_SELECTOR, ".content")
