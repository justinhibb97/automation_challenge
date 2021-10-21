import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from locators import HomePageLocator, RegisterPageLocator, InstitutionPageLocator, SuccessPageLocator

print("#Gemini Coding Challenge")
print("#Contains 12 Tests total testing overall functionality")
print("#By: Justin Hibbard")

#Tests begin here:
class MainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    #Function to check if Element is Present
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    #Test to check if user is able to access Institution Register Page
    def test_navigate_register_page(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()
        assert "[Sandbox] Gemini - Institutional Client Registration" in self.driver.title

    #Test to check if user is able to successfully submit
    #This will fail due to the thanks page being down
    def test_successful_submission(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits successful form checks for success message
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, SuccessPageLocator.successPageBody))

    #Tests to check if user is allowed to submit a blank form
    def test_blank_submission(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits blank form checks for error alert
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing business name
    def test_missing_business_name(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing business name for error
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing company type
    def test_missing_company_type(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing company type for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing state
    def test_missing_state(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing state for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing first name
    def test_missing_first_name(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing first name for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing last name
    def test_missing_last_name(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing last name for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to submit missing email address
    def test_missing_email_address(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form missing email address for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    #Tests to check if user is allowed to email address missing @ symbol
    def test_invalid_email_missing_at(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form with invalid email missing @ for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        #Sending text without @
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("testing.com")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        time.sleep(1)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    # Tests to check if user is allowed to email address missing .com, etc
    def test_invalid_email_missing_dot(self):
        #Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        #Submits form with invalid email missing . for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        #Sending text without .com, etc
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("test@testingcom")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        time.sleep(1)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    # Tests to check if user is allowed to email address missing format
    def test_invalid_email_missing_all(self):
        # Navigates to Register Page
        self.driver.get("https://exchange.sandbox.gemini.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(HomePageLocator.createAccountLink).click()
        self.driver.find_element_by_css_selector(RegisterPageLocator.cookieOkButton).click()
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_xpath(RegisterPageLocator.createBusinessLink).click()

        # Submits form with invalid email missing @ & . for error
        self.driver.find_element_by_name(InstitutionPageLocator.businessNameInput).send_keys("Test LLC")
        self.driver.find_element_by_css_selector(InstitutionPageLocator.companyTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.companyTypeSelection).click()
        self.driver.find_element_by_css_selector(InstitutionPageLocator.stateTypeDropdown).click()
        self.driver.find_element_by_id(InstitutionPageLocator.stateTypeSelection).click()
        self.driver.find_element_by_name(InstitutionPageLocator.firstNameInput).send_keys("First")
        self.driver.find_element_by_name(InstitutionPageLocator.middleNameInput).send_keys("Middle")
        self.driver.find_element_by_name(InstitutionPageLocator.lastNameInput).send_keys("Last")
        # Sending text with invalid format
        self.driver.find_element_by_name(InstitutionPageLocator.emailInput).send_keys("testing")
        self.driver.execute_script("window.scrollTo (0,document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element_by_css_selector(InstitutionPageLocator.continueButton).click()
        time.sleep(1)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, InstitutionPageLocator.errorAlert))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
