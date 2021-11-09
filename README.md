# SM-SeleniumWithPython
Supermarket project uses Selenium with Python for Automation for testing

Setup
1. Install PyCharm
2. Open source (SM-SeleniumWithPython) by PyCharm
3. File > Settings > Project: SM-SeleniumWithPython > Python Interpreter
4. Click icon '+' to add Package:
    + selenium
    + pytest-html
5. Go to Terminal in PyCharm to install Package:
   pip install webdriver_manager
   
6. To run Test Suites:
   pytest -v -s --html=Results\Report.html --self-contained-html  TestSuites