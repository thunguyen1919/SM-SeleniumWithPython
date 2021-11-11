# SM-SeleniumWithPython
Supermarket project uses Selenium with Python for Automation testing

Link website:
http://supermarket-tws.somee.com/

Setup
1. Install PyCharm
2. Open source (SM-SeleniumWithPython) by PyCharm
3. File > Settings > Project: SM-SeleniumWithPython > Python Interpreter
4. Click icon '+' to add Package:
    + selenium
    + pytest-html
5. Go to Terminal in PyCharm to install Package:
   + pip install webdriver_manager
   + pip install openpyxl
   
6. To run Test Suites:
   pytest -v -s --html=Results\Report.html --self-contained-html  TestSuites