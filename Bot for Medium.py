from selenium import webdriver
import time

class OKCBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options)

    def open(self):
        self.driver.get('https://www.okcupid.com/home')

    def sign_in(self):
        time.sleep(3)
        email_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        password_input = self.driver.find_element_by_xpath('//*[@id="password"]')
        email_input.send_keys('someEmail@someDomain.com')
        password_input.send_keys('somepassword')
        next_btn = self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input')
        next_btn.click()

    def swipeRight(self):
        time.sleep(1)
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[2]/div')
        like_btn.click()

    def swipeLeft(self):
        time.sleep(1)
        pass_btn = self.driver.find_element_by_xpath(
            '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[1]/div')
        pass_btn.click()

    def nameChecker(self):
        time.sleep(5)
        name = self.driver.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[1]/div[1]').text
        if name in ['Rachel', 'hanna']:
            self.swipeRight()
            print(name, ' Liked')
        else:
            self.swipeLeft()
            print(name, ' Passed')

# Instantiate Bot
bot = OKCBot()

# Start Session
bot.open()

# Sign-In
bot.sign_in()

# Swiping Left or Right
while True:
    bot.nameChecker()

