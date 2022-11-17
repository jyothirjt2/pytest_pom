import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        edge_opt = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=edge_opt)
        print("launched microsofr edge browser")
        return driver

    elif browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        firefox_opt = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service,options=firefox_opt)
        print("launched firefox browser")
        return driver

    else:
        service = Service(executable_path=ChromeDriverManager().install())
        chrome_opt = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=chrome_opt)
        print("launched chrome browser")
        return driver

def pytest_addoption(parser):        # this method will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                #this will return the browser value to browser in setup method
    request.config.getoption("--browser")

########## to generate pytest HTML reports ########
# hook for adding env info to HTML report
def pytest_configure(config):
    config._metadata['project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'jyothi'

# hook for del/modify env info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


