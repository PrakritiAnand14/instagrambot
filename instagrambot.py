from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot():
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
        else:
            print("You are already following this user")
    
    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")
    
bot = InstagramBot('_.prakkii._', 'prakriti1408')
bot.signIn()
bot.followWithUsername('rado')
