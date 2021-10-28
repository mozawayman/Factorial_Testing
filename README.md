# Factorial_Testing

This repo contains code developed in python for the challenge

To run the projects one should install the virtual environment using the requirements.txt file
(pip install -r requirements.txt)

Then to run the web interface tests, one should use te command as follows:

pytest -v -s tests/UiTests/test_factorial.py --html=<path to save the html report> --browser Chrome/Firefox --driverPath <Path to the specific driver>

To run the EndPoint tests, one should use te command as follows:

pytest -v -s tests/APITests/factorialEndPointTesting.py --html=<path to save the html report> --endPoint http://qainterview.pythonanywhere.com/factorial

Out of curiosity, i made a small naive test with Jmeter to stress  the API,  the .jmx file is present in "BasicDOD" directory
