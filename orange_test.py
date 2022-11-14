import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner #work

class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.close()
    #
    def test_01_login_valid(self):
        self.driver.get("http://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        # 1st test of correct page
        self.assertEqual(self.driver.find_element(By.ID, "txtUsername").get_property("value"), "Admin")
        # 2nd test username_input_field
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.assertEqual(self.driver.find_element(By.ID, "txtPassword").get_property("value"), "admin123")
        #  3rd test password_input_field
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "welcome").click()
        # arrived to the correct page
        self.driver.implicitly_wait(10)
        path_logout = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        path_logout.click()
        #  logout_functionality

    def test_02_login_invalid_username(self):
        self.driver.get("http://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "txtUsername").send_keys("dmin")
        self.assertEqual(self.driver.find_element(By.ID, "txtUsername").get_property("value"), "dmin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.assertEqual(self.driver.find_element(By.ID, "txtPassword").get_property("value"), "admin123")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.driver.find_element(By.ID, "spanMessage").is_displayed())
        self.driver.implicitly_wait(10)

    def test_login_invalid_password(self):
        self.driver.get("http://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.assertEqual(self.driver.find_element(By.ID, "txtUsername").get_property("value"), "Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin13")
        self.assertEqual(self.driver.find_element(By.ID, "txtPassword").get_property("value"), "admin13")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.driver.find_element(By.ID, "spanMessage").is_displayed())
        self.driver.implicitly_wait(10)

    # def test_admin_user_management(self):
    #     self.driver.get("http://opensource-demo.orangehrmlive.com/")
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    #     self.assertEqual(self.driver.find_element(By.ID, "txtUsername").get_property("value"), "Admin")
    #     self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    #     self.assertEqual(self.driver.find_element(By.ID, "txtPassword").get_property("value"), "admin123")
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element(By.ID, "btnLogin").click()
    #     self.driver.implicitly_wait(10)
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
    #     self.driver.find_element(By.NAME, "searchSystemUser[userName]").send_keys("	CecilB")
    #     self.driver.find_element(By.ID, "searchBtn").click()
    #


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTest))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    runner = HtmlTestRunner
    runner.HTMLTestRunner()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())