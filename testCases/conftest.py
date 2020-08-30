from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities


@pytest.fixture()
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    elif browser == "firefox":
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        driver = webdriver.Firefox(capabilities=cap)
        print("Launching Firefox browser")

    else:
        driver = webdriver.Ie()
        print("Launching IE browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##############PyTest HTML Report#############

# It is hook for Adding environment info to HTML report.
def pytest_configure(config):
    config._metadata["Project Name"] = 'nop Commerce'
    config._metadata["Module Name"] = "Customer"
    config._metadata["Tester"] = "Ravi"


# It is hook for delete/modify environment info to HTML report.
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
