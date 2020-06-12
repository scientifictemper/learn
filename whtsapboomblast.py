from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver for chrome browser
caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
driver = webdriver.Chrome(desired_capabilities=caps)
#open website
driver.get('https://web.whatsapp.com/')
input('enter any key after qr scan')
name=input('enter the name:')
#find span tag
accnt=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
accnt.click()
#how many times and msg
n=10
msg='hi'
#chat space
chatbox=driver.find_element_by_class_name('_3uMse')

for i in range(n):
    chatbox.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')#send button
    button.click()
print('completed')