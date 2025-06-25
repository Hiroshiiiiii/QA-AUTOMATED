from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time
import unittest
import random

class DemoBlazeAutomation(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        
        self.rand_num = random.randint(1000, 9999)
        self.username = f"johncarlo{self.rand_num}"
        self.password = "test123"
    
    def tearDown(self):
        self.driver.quit()
    
    def test_complete_workflow(self):
        try:
            self.signup_user()
            
            self.login_user()
            
            self.navigate_site()
            
            self.logout_user()
            
            print("Automation Completed.")
            
        except Exception as e:
            self.fail(f"Complete workflow test failed: {str(e)}")
    
    def signup_user(self):
        print(f"Signing up user: {self.username}")
        
        signup_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
        signup_btn.click()
        
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
        username_field.clear()
        username_field.send_keys(self.username)
        
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))
        password_field.clear()
        password_field.send_keys(self.password)
        
        signup_submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign up')]")))
        signup_submit.click()
        
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Signup alert: {alert_text}")
            alert.accept()
            
            self.assertIn("Sign up successful", alert_text)
            print("✓ Signup successful!")
            
            time.sleep(1)
            
        except TimeoutException:
            self.fail("No alert appeared after signup attempt")
    
    def login_user(self):
        print(f"Logging in user: {self.username}")
        
        login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        login_btn.click()
        
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
        username_field.clear()
        username_field.send_keys(self.username)
        
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "loginpassword")))
        password_field.clear()
        password_field.send_keys(self.password)
        
        login_submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log in')]")))
        login_submit.click()
        
        welcome_msg = self.wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        self.assertIn(f"Welcome {self.username}", welcome_msg.text)
        print("✓ Login successful!")
    
    def navigate_site(self):
        print("Navigating through site categories...")
        
        print("→ Navigating to Phones")
        phones_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones_link.click()
        
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))
        self.assertTrue(product.is_displayed())
        print("✓ Phones category loaded")
        
        print("→ Navigating to Laptops")
        laptops_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops_link.click()
        
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sony vaio i5")))
        self.assertTrue(product.is_displayed())
        print("✓ Laptops category loaded")
        
        print("→ Navigating to Monitors")
        monitors_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Monitors")))
        monitors_link.click()
        
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Apple monitor 24")))
        self.assertTrue(product.is_displayed())
        print("✓ Monitors category loaded")
        
        print("→ Navigating back to Home")
        time.sleep(1)
        home_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Home '] | //a[text()='Home']")))
        home_link.click()
        time.sleep(2)
        print("✓ Home page loaded")
    
    def logout_user(self):
        print("Logging out user...")
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "logout2")))
        print("Logout button found, clicking...")
        logout_btn.click()
        print("Clicked logout, waiting for login button to reappear...")
        login_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "login2")))
        self.assertTrue(login_btn.is_displayed())
        print("✓ Logout successful!")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DemoBlazeAutomation("test_complete_workflow"))
    runner = unittest.TextTestRunner()
    runner.run(suite)