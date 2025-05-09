import requests
import logging
from datetime import datetime

# Configuration
URL = "https://www.flipkart.com/"  # Replace with your app URL
TIMEOUT = 5  # seconds

# Logging setup
logging.basicConfig(
    filename=".venv/app_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_app_health(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        status_code = response.status_code
        if 200 <= status_code < 400:
            msg = f"Application is UP. Status Code: {status_code}"
            print(msg)
            logging.info(msg)
        else:
            msg = f"Application is DOWN. Status Code: {status_code}"
            print(msg)
            logging.warning(msg)
    except requests.exceptions.RequestException as e:
        msg = f"Application is DOWN. Error: {e}"
        print(msg)
        logging.error(msg)

if __name__ == "__main__":
    print(f"\nChecking application health at {datetime.now()}")
    check_app_health(URL)
