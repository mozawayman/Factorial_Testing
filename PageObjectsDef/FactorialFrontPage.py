from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FactorialFrontPage():

    #### WebElement References #######
    pageHeader = (By.CSS_SELECTOR, 'h1.text-center')
    integerInput = (By.ID, 'number')
    calculationButton = (By.CSS_SELECTOR, 'button#getFactorial')
    privacyPageLink =  (By.XPATH, '//a[text()="Privacy"]')
    termsAndConditionsPageLink = (By.XPATH, '//a[text()="Terms and Conditions"]')
    resultString = (By.CSS_SELECTOR, 'p#resultDiv')


    def __init__(self, browser):
        self.browser = browser


    ## defining actions on the page ##

    def getPageHeader(self):
        ''''Wait until page is loaded and extract text from the page'''
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.pageHeader))
        return self.browser.find_element(*self.pageHeader).text


    def inputIntegerForCalculation(self, inputNumber):
        ''''Input parameter for the calculation'''
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.integerInput))
        self.browser.find_element(*self.integerInput).clear()
        self.browser.find_element(*self.integerInput).send_keys(inputNumber)


    def calculateFactorial(self):
        ''''Click the button to request the factorial result'''
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.calculationButton))
        self.browser.find_element(*self.calculationButton).click()


    def getCalculationResultString(self, outputType):
        ''''Return Result String'''
        wait = WebDriverWait(self.browser, 10)
        if outputType == "Result":
            wait.until(EC. text_to_be_present_in_element(self.resultString, "factorial"))
        else:
            wait.until(EC.text_to_be_present_in_element(self.resultString, "Please"))

        return self.browser.find_element(*self.resultString).text


    def goToLinks(self, pageToGo):
        ''''Go to the specific link and return its actual url'''
        wait = WebDriverWait(self.browser, 10)
        if pageToGo == "Privacy" :
            wait.until(EC.element_to_be_clickable(
                self.privacyPageLink)).click()
        else:
            wait.until(EC.element_to_be_clickable(
                self.termsAndConditionsPageLink)).click()

        return self.browser.current_url