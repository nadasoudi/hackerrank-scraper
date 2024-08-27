from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

HACKERRANK_LOGIN_URL = "https://www.hackerrank.com/auth/login"

def login_hackerrank(driver, username, password):
    driver.get(HACKERRANK_URL)
    
    # Wait until the username field is clickable and then input username
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
    ).send_keys(username)
    
    # Wait until the password field is visible and then input password
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    ).send_keys(password)
    
    # Wait until the login button is clickable and then click it
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.c-cUYkx.c-cUYkx-dshqME-variant-primary.c-cUYkx-fGHEql-isFullWidth-true"))
        )
        login_button.click()
    except Exception as e:
        print(f"Error clicking login button: {e}")

def click_cpp_button(driver):
    # Wait for the page to load after login
    time.sleep(5)

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to settle after scrolling

    # Try to find and click the C++ button
    try:
        cpp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='topic-item bold']//div[text()='C++']"))
        )
        ActionChains(driver).move_to_element(cpp_button).click().perform()
        print("Clicked on C++ button successfully!")
    except Exception as e:
        print(f"Error clicking C++ button: {e}")
        print("Current page source:")
        print(driver.page_source)

def main():
    # Your credentials
    username = "for2022n@gmail.com"
    password = "*SKnn5.W7N$KjiL"
    
    # Use chromedriver.exe from the project folder
    driver_path = "chromedriver.exe"
    service = Service(driver_path)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start with maximized window
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        login_hackerrank(driver, username, password)
        print("Login successful!")
        
        click_cpp_button(driver)
        
        # Wait for a moment to see the result
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()