import requests
import pytest


class Test_1_FactorialTestingMakeCalculation:

    @pytest.mark.parametrize("test_input,expectedResult,expectedHTTPCode",
                             [("0", 1,200), ("4",24,200), ("6", 720,200),
("100", 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000,200)])
    def test_checkExpectedFactorialCalculation(self,setup, test_input, expectedResult, expectedHTTPCode):
        '''Evaluate typical success codes for valid input data and its respective answer'''
        payload = {'number': test_input }
        response = requests.post(setup, data=payload)
        assert response.status_code == expectedHTTPCode
        assert response.json()['answer'] == expectedResult


    @pytest.mark.parametrize("test_input,expectedHTTPCode",
                             [("a", "501"), ("", "501"),
                              ("!", "501"), ("1000000000000000000000", "412")])
    def test_checkInvalidFactorialCalculation(self,setup, test_input, expectedHTTPCode):
        '''Evaluate typical error codes for invalid input data'''
        payload = {'number': test_input}
        response = requests.post(setup, data=payload)
        assert response.status_code == expectedHTTPCode