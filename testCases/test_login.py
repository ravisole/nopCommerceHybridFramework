import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()

    logger= LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self, setUp):
        self.logger.info("*****************Test_001_Login***************")
        self.logger.info("*****************Verifying Home Page Title***************")
        self.driver=setUp
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****************Homepage title test is passed.***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
            self.driver.close()
            self.logger.error("*****************Homepage title test is failed.***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUp):
        self.logger.info("*****************Verifying Login Test***************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp= Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*****************Login test is passed.***************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*****************Login test is passed.***************")
            assert False




