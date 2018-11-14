from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import ProjectManage


# Create your tests here.
class ProjectTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user("test01", "test01@mail", "test123456")
        login_data = {'username': "test01", "password": "test123456"}
        response = self.client.post('/login_action/', data=login_data)
        print(response.status_code)

    def test_project_manage(self):
        """项目管理"""
        response = self.client.get('/manage/project_manage/')
        response_html = response.content.decode("utf-8")
        self.assertIn("退出", response_html)
        self.assertIn("测试平台", response_html)


class ProjectAdd(TestCase):
    def setUp(self):
        """添加项目"""
        self.client = Client()
        User.objects.create_user("test01", "test01@mail", "test123456")
        login_data = {'username': "test01", "password": "test123456"}
        response = self.client.post('/login_action/', data=login_data)
        print(response.status_code)

    def test_create_project(self):
        """添加项目成功"""
        data = {"title": "测试新项目", "description": "这是一个测试的新项目，用的djangoTest"}
        response = self.client.post('/manage/add_project/', data=data)
        response_html = response.content.decode("utf-8")
        print(response_html)
        self.assertEqual(response.status_code, 302)


'''
class ProjectEdit(TestCase):
    """测试编辑项目"""
    def setUp(self):
        self.client = Client()
        User.objects.create_user("test01", "test01@mail.com", "test123456")
        login_data = {"username": "test01", "password": "test123456"}
        self.client.post('/login_action/', data=login_data)
        ProjectManage.objects.create(title="测试编辑项目1", description="这是测试编辑的项目1")
        # 创建的项目的id怎么获取？下面这种方式好像不行
        目前无法获取到待编辑的项目id
        pid = ProjectManage.objects.get(title="测试编辑项目1")
        print(pid)

    # def test_edit_project(self, pid):
    #     response = self.client.get('/manage/edit_project/%s/' % pid)
'''