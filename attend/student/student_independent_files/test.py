from selenium import webdriver

options = webdriver.ChromeOptions()

# Define custom headers
headers = {
    "Host": "student.kletech.ac.in",
    "User-Agent": "PostmanRuntime/7.36.3",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Format headers into a string
headers_str = ""
for key, value in headers.items():
    headers_str += f"{key}: {value}\n"

# Disable blink features to allow custom headers
options.add_argument("--disable-blink-features=HeadersOverride")

# Set user agent
options.add_argument(f"--user-agent={headers['User-Agent']}")

# Set host rules
options.add_argument(f"--host-rules={headers['Host']}=127.0.0.1")

# Add headers using user data directory
options.add_argument(f"--user-data-dir={headers_str}")

options.add_argument("--headless=new")
# Instantiate the WebDriver with the configured options
driver = webdriver.Chrome(options=options)
try:
    driver.get("https://student.kletech.ac.in")
    print("got")
except:
    print("error")
