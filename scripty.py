from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("http://wwwadidas.com/yeezy")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'SIZE')]")
while(len(elem)==0):
    elem = driver.find_elements_by_xpath("//*[contains(text(), 'SIZE')]")
    print (elem)
print ("emailed")
