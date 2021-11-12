from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.fixture()
    def login(self, setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        self.driver.execute_script('window.scrollTo(0,300)')
        self.driver.find_element(By.ID, 'UserName').send_keys('ThuNguyen')
        self.driver.find_element(By.ID, 'Password').send_keys('asd@12345')
        self.driver.find_element(By.ID, 'LoginButton').click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[@id="Header_LoginViewHeader_LoginName1"]'),
                                                    "ThuNguyen"))

    def test_buy_products_when_not_logged_in(self, setup):
        self.driver.get('http://supermarket-tws.somee.com/')
        self.driver.find_element(By.LINK_TEXT, 'SHOP NOW').click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1 animated wow slideInLeft'] li[class='active']")))
        self.driver.execute_script('window.scrollBy(0,280)')
        #Add item Fry Pan
        self.driver.find_element(By.XPATH,'//input[@id="MainContent_ItemList_ProductsListView_ctrl0_ButtonAddToCart_0"]').click()

        # Add item Toor Dal
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="MainContent_ItemList_ProductsListView_ctrl0_HyperLink1_2"]')))
        self.driver.execute_script('window.scrollBy(0,280)')
        self.driver.find_element(By.XPATH,'//input[@id="MainContent_ItemList_ProductsListView_ctrl0_ButtonAddToCart_2"]').click()

        #Go to Checkout
        self.driver.find_element(By.XPATH,'//i[@class="fa fa-cart-arrow-down"]').click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1'] li[class='active']")))
        self.driver.execute_script('window.scrollBy(0,180)')

        #Click the Checkout button to go to Login page
        self.driver.find_element(By.ID, 'MainContent_ButtonCheckout').click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.TAG_NAME,'h2'),'LOGIN FORM'))
        self.driver.execute_script('window.scrollBy(0,280)')

    def test_buy_products_when_logged_in(self, setup, login):
        self.driver.find_element(By.LINK_TEXT, 'SHOP NOW').click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1 animated wow slideInLeft'] li[class='active']")))
        self.driver.execute_script('window.scrollBy(0,280)')
        #Add item Fry Pan
        self.driver.find_element(By.XPATH,'//input[@id="MainContent_ItemList_ProductsListView_ctrl0_ButtonAddToCart_0"]').click()

        # Add item Toor Dal
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="MainContent_ItemList_ProductsListView_ctrl0_HyperLink1_2"]')))
        self.driver.execute_script('window.scrollBy(0,280)')
        self.driver.find_element(By.XPATH,'//input[@id="MainContent_ItemList_ProductsListView_ctrl0_ButtonAddToCart_2"]').click()

        #Go to Checkout
        self.driver.find_element(By.XPATH,'//i[@class="fa fa-cart-arrow-down"]').click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ol[class='breadcrumb breadcrumb1'] li[class='active']")))
        self.driver.execute_script('window.scrollBy(0,180)')

        #Click the Checkout button to go to Review Your Order & Complete Checkout page
        self.driver.find_element(By.ID, 'MainContent_ButtonCheckout').click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.TAG_NAME,'h2'),'Review Your Order & Complete Checkout'))