# Выносим локаторы во внешнюю переменную

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BTN = (By.CSS_SELECTOR, 'a[href*="/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "button[name=login_submit]")
    LOGIN_FORM_WELCOME_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")
    REGIST_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGIST_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGIST_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGIST_FORM_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    REGIST_WELCOME_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")


class ProductPageLocators:
    ADD_PROD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type=submit]")
    PROD_TO_BASKET = (By.CSS_SELECTOR, "div#messages :nth-child(1) div strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main :nth-child(1)")
    NAME_ADD_PRODUCT = (By.CSS_SELECTOR, "div#messages :nth-child(1) div :nth-child(1)")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main :nth-child(2)")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div#messages :nth-child(3) div.alertinner :nth-child(1) :nth-child(1)")
    PRICE_IN_TOP = (By.CSS_SELECTOR, "div.basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Ваша корзина пуста")]')
