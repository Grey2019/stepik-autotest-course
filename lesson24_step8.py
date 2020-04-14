#http://suninjuly.github.io/simple_form_find_task.html

from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    button = browser.find_element_by_id("book") #Find and Click button on the page
	
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))
    button.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_id('solve')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
#lesson24_step8.py