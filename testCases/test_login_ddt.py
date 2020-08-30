import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities
import time


class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//Test Data/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setUp):
        self.logger.info("***********TestLogin DDT02**************")
        self.logger.info("*****************Verifying Login DDT Test***************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtilities.getRowCount(self.path, 'Sheet1')
        print("Number of rows in a excel", self.rows)

        lst_status = []  # Empty list

        for r in range(2, self.rows + 1):
            self.user = XLUtilities.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilities.readData(self.path, 'Sheet1',r,2)
            self.exp= XLUtilities.readData(self.path, 'Sheet1',r,3)
            print(self.user)
            print(self.password)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****************Login test is passed.***************")
                    self.lp.clickLogout()
                    time.sleep(10)
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("***************Failed**************")
                    self.lp.clickLogout()
                    time.sleep(10)
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****************Login test is Failed.***************")
                    time.sleep(10)
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("***************Login test is Passed**************")
                    time.sleep(10)
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login ddt is passed")
            print("Login ddt is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login ddt is Failed")
            print("Login ddt is failed")
            self.driver.close()
            assert False

        self.logger.info("-------End of Login DDT Test-------")
        self.logger.info("-------Completed TC_LoginDDT_002")
