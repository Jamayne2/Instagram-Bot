import selenium
from selenium import webdriver
import os
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:
    def __init__(self, username ,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')

    def closedBrowsrer(self):
        self.driver.close()



    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        time.sleep(5)

        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)

        
    def like_message(self):
        

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()
        time.sleep(5)

        if self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div'):
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        else:
            print("Print Not found")
        try:
            for i in range(1, 10):
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article[{}]/div[3]/section[1]/span[1]/button'.format(i)).click()
        except:
            print("Double Post")





igbot = InstagramBot("username" , "password")
igbot.login()
igbot.like_message()

print(igbot.username)