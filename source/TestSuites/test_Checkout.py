from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestCheckout():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()