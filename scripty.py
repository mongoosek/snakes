import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

output = "undefined"

def send_simple_message():
    os.system("curl -s --user 'api:key-1d83a78fef75bfe2aa4f90449f464e69' \
    https://api.mailgun.net/v3/sandboxd41db11df9e54aa8b9b9474fb6af27e0.mailgun.org/messages \
        -F from='Mailgun Sandbox <mailgun@sandboxd41db11df9e54aa8b9b9474fb6af27e0.mailgun.org>' \
        -F to='Rohan <rohandhesikan@gmail.com>' \
        -F subject='We hit "+output+"' \
        -F text='Log in ASAP'")
p = subprocess.Popen(["hostname -I"], shell=True, stdout=subprocess.PIPE)
output = p.stdout.read()
print output


driver = webdriver.Chrome()
driver.get("http://www.adidas.com/yeezy")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'SIZE CHART')]")
while(len(elem)==0):
    elem = driver.find_elements_by_xpath("//*[contains(text(), 'SIZE CHART')]")
send_simple_message()
print 'detected'



