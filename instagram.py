
from instagramUserİnfo import email, password
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
class İnstagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
    def signIn(self):
        
        self.browser.get("https://www.instagram.com")
        time.sleep(3)
        emailInput = self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        
        
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
instgram = İnstagram(email, password)
instgram.signIn()
