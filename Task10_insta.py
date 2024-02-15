from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstagramProfileScraper:
    def __init__(self, profile_url):
        self.profile_url = profile_url
        self.driver = webdriver.Chrome()

    def extract_followers_following(self):
        self.driver.get(self.profile_url)
        try:
            # Wait for the profile page to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "-vDIg")))

            # Find the followers and following elements using relative XPath
            followers_element = self.driver.find_element(By.XPATH, "//ul[@class='k9GMp ']/li[2]//a/span")
            following_element = self.driver.find_element(By.XPATH, "//ul[@class='k9GMp ']/li[3]//a/span")

            # Extract the text containing the number of followers and following
            followers_count = followers_element.text
            following_count = following_element.text

            return followers_count, following_count

        finally:
            # Close the browser window
            self.driver.quit()


# Instantiate the InstagramProfileScraper class
profile_scraper = InstagramProfileScraper("http://www.instagram.com/guviofficial/")

# Extract followers and following counts
followers, following = profile_scraper.extract_followers_following()
print("Followers:", followers)
print("Following:", following)