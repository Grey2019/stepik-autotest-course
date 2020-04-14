from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
try:
    button = browser.find_element_by_id("button")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

#lesson24_step6.py