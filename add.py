
# add a student to a class
from selenium import webdriver
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome('/Users/user/Downloads/chromedriver')
browser.get('https://www.eschool.edu.ps')

browser.find_element_by_xpath('(//*[@title="إضافة"])[1]').click()
#id
id = browser.find_element_by_id('ID')
id.send_keys('850654104')

#student number
user_code = browser.find_element_by_id('user_code')
user_code.send_keys('850654104')

#student name ar
name_ar = browser.find_element_by_id('name_ar')
name_ar.send_keys('علي محمد خالد')

#student name en
name_en = browser.find_element_by_id('name_en')
name_en.send_keys('علي محمد خالد')

#student country of birth
birth_country =Select(browser.find_element_by_id('birth_country'))
birth_country.select_by_value('1')









