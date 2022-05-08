from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ObjectPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[value]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
