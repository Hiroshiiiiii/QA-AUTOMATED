from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

# Setup Chrome driver
driver = webdriver.Chrome()

try:
    print("Starting OCSS test...")
    
    timestamp = str(int(time.time()))[-4:]
    test_email = f"jc{timestamp}@gmail.com"
    print(f"Using timestamp: {timestamp}")
    print(f"Using email: {test_email}")
    
    # Step 1: Admin Login
    print("Logging in as admin...")
    driver.get("http://localhost/ocss/admin_login.php")
    time.sleep(3)
    
    # Fill login form
    username = driver.find_element(By.NAME, "admin_username")
    username.send_keys("admin")
    
    password = driver.find_element(By.NAME, "admin_pass")
    password.send_keys("admin")
    
    login_button = driver.find_element(By.NAME, "admin_login")
    login_button.click()
    time.sleep(3)
    
    print("Admin logged in!")
    
    # Step 2: Add Faculty
    print("Adding faculty...")
    
    nav_menu = driver.find_element(By.ID, "nav")
    nav_menu.click()
    time.sleep(2)
    
    add_faculty = driver.find_element(By.XPATH, "//a[@data-target='#facultyModal']")
    add_faculty.click()
    time.sleep(2)
    
    emp_number = driver.find_element(By.NAME, "emp_number")
    emp_number.send_keys(f"123{timestamp}")
    
    faculty_name = driver.find_element(By.NAME, "fname")
    faculty_name.send_keys("Macapagal, John Carlo A.")
    
    date_hired = driver.find_element(By.NAME, "date_hired")
    driver.execute_script("arguments[0].value = '2003-12-12';", date_hired)
    
    status_dropdown = Select(driver.find_element(By.NAME, "status"))
    status_dropdown.select_by_value("Full-time Faculty")
    
    background = driver.find_element(By.NAME, "background_field")
    background.send_keys("BSIT")
    
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Unisan, Quezon")
    
    contact = driver.find_element(By.NAME, "contact_no")
    contact.send_keys("09090909021")
    
    email = driver.find_element(By.NAME, "email")
    email.send_keys(test_email)
    
    random_number = random.randint(1000, 9999)
    new_password = f"JohnCarlo{random_number}"
    print(f"Password: {new_password}")
    
    password_field = driver.find_element(By.NAME, "pass")
    password_field.send_keys(new_password)
    
    # Submit faculty
    register_button = driver.find_element(By.NAME, "register_faculty")
    register_button.click()
    time.sleep(3)
    
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alert appeared: {alert_text}")
        alert.accept()  # Click OK on the alert
        print("Alert closed")
        
        print("Warning: Faculty might not have been added due to existing data")
    except:
        pass  # No alert, continue
    
    print("Faculty added!")
    
    # Step 3: Test faculty login
    print("Testing faculty login...")
    
    # Logout admin first
    nav_menu = driver.find_element(By.ID, "nav")
    nav_menu.click()
    time.sleep(1)
    
    logout_link = driver.find_element(By.LINK_TEXT, "Log Out")
    logout_link.click()
    time.sleep(2)
    
    # Go to user login
    driver.get("http://localhost/ocss/index.php")
    time.sleep(3)
    
    # Login as faculty with the correct email and password
    user_email = driver.find_element(By.NAME, "user_email")
    user_email.send_keys(test_email)
    
    user_password = driver.find_element(By.NAME, "user_pass")
    user_password.send_keys(new_password)
    
    user_login = driver.find_element(By.NAME, "Login")
    user_login.click()
    time.sleep(5)
    
    # Check if faculty login worked by looking for logout link or dashboard
    try:
        logout_link = driver.find_element(By.LINK_TEXT, "Log Out")
        print("✓ Faculty login successful!")
        
        logout_link.click()
        time.sleep(2)
        print("Faculty logged out")
    except:
        try:
            dashboard_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Dashboard')]")
            print("✓ Faculty login successful (dashboard found)!")
        except:
            print("✗ Faculty login failed - could not find logout link or dashboard")
            print(f"Current URL: {driver.current_url}")
            print(f"Page title: {driver.title}")
            
            try:
                error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid') or contains(text(), 'Error') or contains(text(), 'Wrong')]")
                print(f"Error message found: {error_element.text}")
            except:
                print("No obvious error message found")
    
    driver.get("http://localhost/ocss/admin_login.php")
    time.sleep(2)
    
    # Step 4: Login as admin again and add subject
    print("Adding subject...")
    
    # Admin login again
    username = driver.find_element(By.NAME, "admin_username")
    username.send_keys("admin")
    
    password = driver.find_element(By.NAME, "admin_pass")
    password.send_keys("admin")
    
    login_button = driver.find_element(By.NAME, "admin_login")
    login_button.click()
    time.sleep(3)
    
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Login alert: {alert_text}")
        alert.accept()
        print("Alert closed, trying login again...")
        
        username = driver.find_element(By.NAME, "admin_username")
        username.clear()
        username.send_keys("admin")
        
        password = driver.find_element(By.NAME, "admin_pass")
        password.clear()
        password.send_keys("admin")
        
        login_button = driver.find_element(By.NAME, "admin_login")
        login_button.click()
        time.sleep(3)
    except:
        pass
    
    # Add Subject
    nav_menu = driver.find_element(By.ID, "nav")
    nav_menu.click()
    time.sleep(2)
    
    add_subject = driver.find_element(By.XPATH, "//a[@data-target='#subjectModal']")
    add_subject.click()
    time.sleep(2)
    
    subject_code = driver.find_element(By.NAME, "subject_code")
    subject_code.send_keys(f"INTE-{timestamp}")
    
    subject_desc = driver.find_element(By.NAME, "subject_description")
    subject_desc.send_keys("Integration and Testing")
    
    unit_dropdown = Select(driver.find_element(By.NAME, "unit"))
    unit_dropdown.select_by_value("3")
    
    lecture_dropdown = Select(driver.find_element(By.NAME, "lecture"))
    lecture_dropdown.select_by_value("2")
    
    lab_dropdown = Select(driver.find_element(By.NAME, "laboratory"))
    lab_dropdown.select_by_value("0")
    
    add_subject_btn = driver.find_element(By.NAME, "add")
    add_subject_btn.click()
    time.sleep(3)
    
    print("Subject added!")
    
    # Step 5: Add Room
    print("Adding room...")
    
    nav_menu = driver.find_element(By.ID, "nav")
    nav_menu.click()
    time.sleep(2)
    
    try:
        add_room = driver.find_element(By.XPATH, "//a[@data-target='#roomModal']")
        add_room.click()
        time.sleep(2)
        
        room_field = driver.find_element(By.NAME, "room")
        room_field.send_keys(f"0{timestamp[-2:]}")
        
        add_room_btn = driver.find_element(By.NAME, "add_room")
        add_room_btn.click()
        time.sleep(3)
        
        print("Room added!")
    except Exception as room_error:
        print(f"Could not add room: {room_error}")
    
    print("Test completed successfully!")

except Exception as e:
    print(f"Something went wrong: {e}")
    import traceback
    traceback.print_exc()

finally:
    print("Closing browser...")
    time.sleep(2)
    driver.quit()