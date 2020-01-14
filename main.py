from selenium import webdriver
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome('/Users/user/Downloads/chromedriver')
browser.get('https://www.eschool.edu.ps')


#Drop a student from a grade in archive
for i in range(300):
    browser.find_element_by_xpath('(//*[@title="تسرب"])[1]').click()
    browser.switch_to_alert().accept()


#Accept number of i of students in a grade 

for i in range(1,10):
    browser.find_element_by_id('checkbox'+str(i)).click()
    dropdown = Select(browser.find_element_by_id('gradeToWaitingForAprove'+str(i)))
    dropdown.select_by_visible_text('العاشر ا / الأساسي')
browser.find_element_by_xpath('//*[@id="acceptt"]/table/tbody/tr[3]/td/div/div/div[2]').click()




