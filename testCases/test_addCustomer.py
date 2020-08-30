import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setUp):
        self.logger.info("**********Test 03 Add Customer**************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login Successful*************")
        self.logger.info("**********Starting Add Customer Test******")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomersMenu()
        time.sleep(2)
        self.addCust.clickCustomersMenuItem()

        self.addCust.clickOnAddNew()

        self.logger.info("*************Providing Customer info***********")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Guest")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("John")
        self.addCust.setLastName("Rao")
        self.addCust.setDob("09/11/1990")  # Format DD/MM/YYYY
        self.addCust.setCompanyName("ApniKhudKi")
        self.addCust.setAdminContent("This is for testing........")
        self.addCust.clickSave()

        self.logger.info("***********Saving Customer Info**********")
        self.logger.info("************Add Customer validation has started.****")
        time.sleep(3)
        msg=self.addCust.getMessageText()
        self.logger.info(msg)
        print(msg)

        if "The new customer has been added successfully." in msg:
            assert True
            self.logger.info("Test Case is Passed.")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********Add customer test failed********")
            assert False

        self.driver.close()
        self.logger.info("**********Ending homepage title test********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
