from PageObjectsDef.FactorialFrontPage import FactorialFrontPage
import pytest


class Test_0_FactorialTestingUI:


    def test_checkPageHeader(self,setup):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        assert pageReferance.getPageHeader() == "The greatest factorial calculator!"


    def test_checkTermsLink(self, setup):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        assert "terms" in pageReferance.goToLinks("terms")


    def test_checkPrivacyLink(self, setup):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        assert "privacy" in pageReferance.goToLinks("Privacy")



class Test_1_FactorialTestingMakeCalculation:

    @pytest.mark.parametrize("test_input,expected", [("0", "1"), ("4","24"), ("6", "720")])
    def test_checkExpectedFactorialCalculation(self,setup, test_input, expected):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        pageReferance.inputIntegerForCalculation(test_input)
        pageReferance.calculateFactorial()
        assert expected in pageReferance.getCalculationResultString("Result")


    @pytest.mark.parametrize("test_input,expected",
     [("a", "Please enter an integer"), ("", "Please enter an integer"), ("!", "Please enter an integer")])
    def test_checkErrorFactorialCalculation(self,setup, test_input, expected):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        pageReferance.inputIntegerForCalculation(test_input)
        pageReferance.calculateFactorial()
        assert expected in pageReferance.getCalculationResultString("Error")


    @pytest.mark.parametrize("test_input,expected",[("300", "Infinity"), ("1000", "Infinity")])
    def test_checkBigNumberFactorialCalculation(self, setup, test_input, expected):
        driver = setup[0]
        pageReferance = FactorialFrontPage(driver)
        pageReferance.inputIntegerForCalculation(test_input)
        pageReferance.calculateFactorial()
        assert expected in pageReferance.getCalculationResultString("Result")