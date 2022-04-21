
class login:
    username_id = 'Email'
    password_id = 'Password'
    click_login_xpath = "//button[contains(text(),'Log in')]"
    logout_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver

    def username(self,username):
        self.driver.By.Id(self.username_id).clear()
        self.driver.By.Id(self.username_id).send_keys(username)

    def password(self,passwaord):
        self.driver.By.Id(self.password_id).clear()
        self.driver.By.Id(self.password_id).send_key(passwaord)

    def clickLogin(self):
        self.driver.By.Xpath(self.click_login_xpath).click()

    def clickLogout(self):
        self.driver.By.LinkText(self.logout_linktext).click()

