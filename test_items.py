from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exist(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    # время на визуальную проверку языка страницы
    time.sleep(5)
    # проверка наличия кнопки добавления в корзину
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), "No Add to basket button found"
