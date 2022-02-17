from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from task2.pages.locators import *


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    input_field = (By.ID, INPUT_FIELD)
    submit_button = (By.XPATH, SUBMIT_BUTTON)
    search_result = (By.CSS_SELECTOR, SEARCH_RESULT)
    adv_search = (By.CSS_SELECTOR, ADVANCED_SEARCH)
    doc_type = (By.ID, DOC_TYPE)
    jpg_img = (By.XPATH, JPG_IMG)

    def search_by_default(self, text):
        search_field = self.driver.find_element(*SearchPage.input_field)
        search_button = self.driver.find_element(*SearchPage.submit_button)
        search_field.send_keys(text)
        search_button.click()
        return self.driver.find_element(*SearchPage.search_result)

    def advanced_search_not_these_words(self, search_text):
        self.driver.implicitly_wait(10)
        search_field = self.driver.find_element(*SearchPage.input_field)
        search_button = self.driver.find_element(*SearchPage.submit_button)
        doc = self.driver.find_element(*SearchPage.doc_type)
        # Advanced search dialog
        self.driver.find_element(*SearchPage.adv_search).click()
        # Doc type
        ActionChains(self.driver).move_to_element(doc).click().perform()
        # Choose doc type
        jpg_img = self.driver.find_element(*SearchPage.jpg_img)
        ActionChains(self.driver).move_to_element(jpg_img).click().perform()
        # Fill search field
        search_field.send_keys(search_text)
        search_button.click()
        return self.driver.find_element(*SearchPage.search_result)


