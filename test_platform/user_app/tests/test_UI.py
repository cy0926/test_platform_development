# -*-coding:utf-8-*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import ProjectManage


class LoginTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """初始化数据"""
        User.objects.create_user("test01", "test01@mail.com", "test123456")
        ProjectManage.objects.create(title="测试平台项目", description="描述")

    def test_login_empty(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("")
        sleep(1)
        self.driver.find_element_by_id("LoginButton").click()
        error_hint = self.driver.find_element_by_id("error").text
        print(error_hint)
        self.assertEqual("用户名或密码为空", error_hint)

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("error_username")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("error_password")
        sleep(1)
        self.driver.find_element_by_id("LoginButton").click()
        error_hint = self.driver.find_element_by_id("error").text
        print(error_hint)
        self.assertEqual("用户名密码错误", error_hint)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("admin")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("admin")
        sleep(1)
        self.driver.find_element_by_id("LoginButton").click()
        username = self.driver.find_element_by_id("user").text
        print(username)
        # 判断登录名是否是admin
        self.assertEqual("admin", username)


