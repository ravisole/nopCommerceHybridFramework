import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_005:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger= LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("***************SearchCustomerByEmail_004*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName()
        self.lp.setPassword()
        self.lp.clickLogin()

        self.logger.info("***********Starting Search Customer By Email**********")
        self.addCust= AddCustomer(self.driver)
        self.addCust.clickCustomersMenu()
        self.addCust.clickCustomersMenuItem()

        self.logger.info("************Seach Customer By Email Id********")
        searchCust= SearchCustomer(self.driver)
        searchCust.setFirstName("Ravishankar")
        searchCust.clickSearchButton()
        time.sleep(5)
        status= searchCust.searchCustomerByName("admin@nopCommerce.com")
        assert True==status
        self.logger.info("********** TC_SearchCustomerByName Finished ************")
        self.driver.close