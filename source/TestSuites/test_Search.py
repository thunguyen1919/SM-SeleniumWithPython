from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearch():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_do_not_enter_keywords(self, setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.XPATH, '//i[@class="fa fa-search"]').click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1 animated wow slideInLeft'] li[class='active']")))
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class="snipcart-item block"]')))

    def test_enter_keyword_the_product_exists(self, setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.ID, 'TextBoxKeyword').send_keys('Tropicana')
        self.driver.find_element(By.XPATH, '//i[@class="fa fa-search"]').click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1 animated wow slideInLeft'] li[class='active']")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="Tropicana"]')))

    def test_enter_keyword_product_does_not_exists(self, setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.ID, 'TextBoxKeyword').send_keys('asd')
        self.driver.find_element(By.XPATH, '//i[@class="fa fa-search"]').click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1 animated wow slideInLeft'] li[class='active']")))
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class="snipcart-item block"]')))