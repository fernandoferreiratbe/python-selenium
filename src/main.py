from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


@dataclass
class Address:
    street: str
    district: str
    city: str
    zipcode: str

    def __str__(self):
        return f"""\nStreet: {self.street}\nDistrict: {self.district}\nCity: {self.city}\nZipcode: {self.zipcode}\n"""


def get_address_from_cep(_cep: str):
    # Start a WebDriver service
    # Specify the path to your chromedriver. In this case it is on macOS
    service = Service('/usr/local/bin/chromedriver')
    service.start()

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service)

    try:
        # Open Correios website
        driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")

        # Find the CEP input field and send the CEP
        cep_input = driver.find_element(by=By.ID, value='endereco')
        cep_input.send_keys(_cep)
        cep_input.send_keys(Keys.RETURN)

        # Wait for a moment to ensure the page is fully loaded
        time.sleep(2)

        # Find the address element
        _street = driver.find_element(By.XPATH, value='//*[@id="resultado-DNEC"]/tbody/tr[1]/td[1]')
        _district = driver.find_element(By.XPATH, value='//*[@id="resultado-DNEC"]/tbody/tr[1]/td[2]')
        _city = driver.find_element(By.XPATH, value='//*[@id="resultado-DNEC"]/tbody/tr[1]/td[3]')
        _zipcode = driver.find_element(By.XPATH, value='//*[@id="resultado-DNEC"]/tbody/tr[1]/td[4]')

        return Address(street=_street.text.strip(),
                       district=_district.text.strip(),
                       city=_city.text.strip(),
                       zipcode=_zipcode.text.strip()
                       )
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        # Close the browser
        driver.quit()
        # Stop the WebDriver service
        service.stop()


# Example usage
cep = input("Enter the CEP: ")
address = get_address_from_cep(cep)
if address:
    print("Address:", address)
else:
    print("Failed to retrieve address.")
