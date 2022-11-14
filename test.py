import time
from selenium import webdriver

driver = webdriver.Chrome()

def first_test():
    driver.maximize_window()
    driver.get('https://ya.ru/')

    # все сервисы
    service = driver.find_element("xpath", "//a[@title='Все сервисы']")
    service.click()

    # переход в яндекс маркет
    market = driver.find_element("xpath", "//a[@data-statlog='services_pinned.more_popup.item.market']").click()
    market_page = driver.window_handles[1]
    driver.switch_to.window(market_page)

    time.sleep(10)

    # каталог
    catalog = driver.find_element("xpath", "//button[@id='catalogPopupButton']")
    catalog.click()
    time.sleep(5)

    # смартфоны
    phone = driver.find_element("xpath", "//a[@href='/catalog--smartfony/61808/list?promo-type=market&hid=91491&glfilter=16816262%3A16816264']")
    phone.click()
    time.sleep(5)

    # до 5 дней
    driver.find_element("xpath", "//input[@value='delivery-interval_5']").click()
    time.sleep(3)

    # 5 моделей
    driver.find_element("xpath", "//input[@name='xvqqtgrok2j_7701962']").click()
    time.sleep(2)

    driver.find_element("xpath", "//input[@name='m2y7xwuntib_153061']").click()
    time.sleep(2)

    driver.find_element("xpath", "//input[@name='m2y7xwuntib_153043']").click()
    time.sleep(2)

    driver.find_element("xpath", "//input[@name='m2y7xwuntib_10556303']").click()
    time.sleep(2)

    driver.find_element("xpath", "//input[@name='m2y7xwuntib_16713696']").click()
    time.sleep(2)

if __name__ == '__main__':
    first_test()

