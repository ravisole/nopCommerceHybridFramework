import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    lnkCustomer_menu_xpath="//a[@href='#']//span[contains(text(), 'Customers')]"
    lnkCustomer_menuItem_xpath= "//span[@class='menu-item-title'][contains(text(), 'Customers')]"
    btnAddnew_xpath= "//a[@class='btn bg-blue']"

    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_id= 'Gender_Male'
    rdFemaleGender_id='Gender_Female'
    txtDateofBirth_xpath= "//input[@id='DateOfBirth']"
    txtCompanyName_id='Company'
    cbIsTaxExempt_id= 'IsTaxExempt'
    txtCustomerRoles_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']//parent::div"
    lstitemAdministrator_xpath="//li[contains(text(), 'Administrator']"
    lstitemRegistered_xpath= "//li[contains(text(), 'Registered]"
    lstitemForum_Moderators_xpath= "//li[contains(text(), 'Forum Moderators']"
    lstitemGuests_xpath= "//li[contains(text(), 'Guests')]"
    lstitemVendors_xpath= "//li[contains(text(), 'Vendors']"
    drpmgrOfVendor_xpath= "//*[@id='VendorId']"
    cbActive_xpath= "//input[@id='Active']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath ="//button[@name= 'save']"
    btnSaveContinue_xpath="//button[@name= 'save-continue']"

    def __init__(self, driver):
        self.driver= driver

    def clickCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)

        if role=='Registered':
            self.listitem= self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem= self.driver.find_element_by_xpath(self.lstitemAdministrator_xpath)
        elif role=='Guest':
            time.sleep(3)
            #self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']").click()
            self.driver.find_element_by_xpath("//li[@class='k-button']//span[@class='k-select']").click()
            self.listitem= self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        elif role== 'Registered':
            self.listitem= self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role== 'Forum Moderators':
            self.listitem= self.driver.find_element_by_xpath(self.lstitemForum_Moderators_xpath)
        else:
            self.listitem= self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp= Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):

        if gender=='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

        elif gender== 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()

        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDateofBirth_xpath).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(compname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(content)

    def clickActive(self):
        self.driver.find_element_by_xpath(self.cbActive_xpath).click()

    def clickIsTaxExempt(self):
        self.driver.find_element_by_id(self.cbIsTaxExempt_id).click()

    def clickSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def getMessageText(self):
       return self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").get_attribute('innerHTML')









    

    