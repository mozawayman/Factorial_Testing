import pytest
from selenium.webdriver import Chrome as chromeWebDriver
from selenium.webdriver import Firefox as firefoxWebDriver

@pytest.fixture
def setup(endPointConf):
    return endPointConf

def pytest_addoption(parser):
    parser.addoption("--endPoint")

@pytest.fixture
def endPointConf(request):
    return request.config.getoption("--endPoint")

## Hooks for HTML Report ##

def pytest_configure(config):
    config._metadata['Project Name'] = 'HostelWorld QA'
    config._metadata['Module Name'] = 'HostelWorld Factorial Calculator API'
    config._metadata['Tester'] = 'John'
