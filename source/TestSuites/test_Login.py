import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from Resources import XLUtils


class TestLogin():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_login_suite(self,setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        pathin = 'TestData\\data.xlsx'
        pathout = 'Results\\result.xlsx'
        sheet = "Sheet1"
        rows = XLUtils.getRowCount(pathin, sheet)
        for r in range(2, rows + 1):
            username = XLUtils.readData(pathin, sheet, r, 1)
            password = XLUtils.readData(pathin, sheet, r, 2)
            xpath = XLUtils.readData(pathin, sheet, r, 3)
            output = XLUtils.readData(pathin, sheet, r, 4)

            self.driver.execute_script('window.scrollTo(0,300)')
            self.driver.find_element(By.ID, 'UserName').clear()
            self.driver.find_element(By.ID, 'Password').clear()

            self.driver.find_element(By.ID, 'UserName').send_keys(username)
            self.driver.find_element(By.ID, 'Password').send_keys(password)

            self.driver.find_element(By.ID, 'LoginButton').click()
            try:
                wait = WebDriverWait(self.driver, 30)
                wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), output))
                XLUtils.writeData(pathout, 'Sheet1', r, 5, 'PASS')
            except Exception as ex:
                print(ex)
                XLUtils.writeData(pathout, 'Sheet1', r, 5, 'FAIL')
