from selenium import webdriver

# Path to the GeckoDriver executable (for Firefox)  # Replace with your actual path

# Create a new instance of FirefoxDriver
driver = webdriver.Firefox()

# Open a webpage
driver.get("https://www.example.com")

# Get the current URL of the webpage
current_url = driver.current_url
print("Current URL:", current_url)

# Close the browser
driver.quit()
