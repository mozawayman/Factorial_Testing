import pytest
from selenium.webdriver import Chrome as chromeWebDriver
from selenium.webdriver import Firefox as firefoxWebDriver

@pytest.fixture
def setup(browserConf):
    if browserConf[0]=='Chrome':
        driver = chromeWebDriver(executable_path=browserConf[1])
    elif browserConf[0]=='Firefox':
        driver = firefoxWebDriver(executable_path=browserConf[1])
    else:
        raise AttributeError("Browser config not yet Supported, as of now only (Firefox and Chrome)")

    baseURL = "http://qainterview.pythonanywhere.com/"
    driver.get(baseURL)
    return (driver,baseURL)

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--driverPath")

@pytest.fixture
def browserConf(request):
    return (request.config.getoption("--browser"), request.config.getoption("--driverPath"))

@pytest.fixture
def tearDown(setup):
    browserQuit = setup[0]
    yield browserQuit
    browserQuit.quit()

## Hooks for HTML Report ##

def pytest_configure(config):
    config._metadata['Project Name'] = 'HostelWorld QA'
    config._metadata['Module Name'] = 'HostelWorld Factorial Calculator UI'
    config._metadata['Tester'] = 'John'
