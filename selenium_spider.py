from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
input_str=browser.find_element_by_id('q')
input_str.send_keys('ipad')
time.sleep(3)
input_str.clear()
input_str.send_keys('iphone')
button=browser.find_element_by_css_selector('btn-serach tb-bg')
button.click()



browser.close()