from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path='./geckodriver')

try:
    # driver.implicitly_wait(10) # seconds
    print('try-dadi')
    driver.get('https://www.google.com/')

    sleep(2)

    search_input = driver.find_element_by_name('q')

    search_input.send_keys('python')

    # sleep(2)

    search_button = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.tfB0Bf > center > input.gNO89b')

    search_button.click()
except:
    print('error bas verdi')
finally:
    print('finally-e daxil oldu')
    sleep(4)
    driver.close()

