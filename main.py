from selenium import webdriver
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome('/Users/user/Downloads/chromedriver')
browser.get('https://www.eschool.edu.ps')


#Drop a student from a grade in archive
for i in range(300):
    browser.find_element_by_xpath('(//*[@title="تسرب"])[1]').click()
    browser.switch_to_alert().accept()


#Accept a student in grade 1 in archive
for i in range(3):
    browser.find_element_by_xpath('//*[@id="acdnmenu"]/ul/li[3]/div').click()
    radio = browser.find_element_by_id('checkbox1')
    radio.click()
    dropdown =Select(browser.find_element_by_id('gradeToWaitingForAprove1'))
    dropdown.select_by_visible_text('الأول أ / الأساسي')
    browser.find_element_by_xpath('//*[@id="acceptt"]/table/tbody/tr[3]/td/div/div/div[2]').click()


