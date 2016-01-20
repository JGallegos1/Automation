from selenium import webdriver

print('Input your LinkedIn email address')
userEmail = input()
print('Input your LinkedIn password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/')

emailElem = browser.find_element_by_id('login-email')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('login-password')
passwordElem.send_keys(userPassword)
passwordElem.submit()