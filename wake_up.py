from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- CONFIGURATION ---
APP_URL = "https://YOUR-APP-NAME.streamlit.app"  # <--- PUT YOUR URL HERE
# ---------------------

def wake_up_app():
    print("Initializing Headless Chrome...")
    
    # Setup Chrome options for running in a cloud server (Headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Install and setup the browser driver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"Navigating to {APP_URL}...")
        driver.get(APP_URL)
        
        # Wait for the page to load (Streamlit can be slow)
        time.sleep(5) 

        # Check for the specific "Yes" button
        # This XPATH looks for a button that contains the specific text
        xpath = "//button[contains(., 'Yes, get this app back up')]"
        buttons = driver.find_elements(By.XPATH, xpath)

        if buttons:
            print("💤 Sleep detected! Clicking the wake up button...")
            buttons[0].click()
            time.sleep(5) # Wait for click to register
            print("✅ Clicked! App should be waking up now.")
        else:
            print("👀 'Yes' button not found. The app is likely already awake.")
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        driver.quit()
        print("Driver closed.")

if __name__ == "__main__":
    wake_up_app()
