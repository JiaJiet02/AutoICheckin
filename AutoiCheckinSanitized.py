from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Step 1: Ask for attendance code input from the user
attendance_code = input("Please enter the attendance code: ")

# Step 2: Launch a browser program like Microsoft Edge
driver = webdriver.Edge()  # or webdriver.Chrome() for Chrome, etc.

# Step 3: Visit the website "www.attendance.com"
driver.get("https://izone.sunway.edu.my/")

# Step 4: Log into the website by filling out account credentials
username = "username_here"
password = "password_here"

username_field = driver.find_element(By.ID, "student_uid")  # Locate username field
password_field = driver.find_element(By.ID, "password")  # Locate password field

username_field.send_keys(username)  # Fill in username
password_field.send_keys(password)  # Fill in password

login_button = driver.find_element(By.ID, "submit")  # Locate login button
login_button.click()  # Click login button

# Step 5: Navigate to the attendance section by clicking the attendance zone button
attendance_zone_button = driver.find_element(By.ID, "iCheckInUrl")
attendance_zone_button.click()

# Step 6: Fill out the attendance zone with the attendance code input from the user
attendance_zone_input = driver.find_element(By.ID, "checkin_code")
attendance_zone_input.send_keys(attendance_code)

# Step 7: Click the button to submit the code
submit_button = driver.find_element(By.ID, "iCheckin")
submit_button.click()

test = input ("Success?: ")

# Close the browser
driver.quit()