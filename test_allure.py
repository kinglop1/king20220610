import os
import allure
import pytest

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景001，微信用户注册')
@allure.title('测试用例001：通过微信正常注册男用户')
def test_case01():
    assert 1==1
    # 上传图片
    # with allure.step('第一个用例'):
    #     with open('./img/1.png','rb') as f:
    #         img = f.read()
    #     allure.attach(img,'展昭')

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景001，微信用户注册')
@allure.title('测试用例002：通过微信正常注册女用户')
def test_case02():
    assert 1==1

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景002，微信用户注册校验')
@allure.title('测试用例003：用户名为空提交注册信息')
def test_case03():
    assert 1==3

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景002，微信用户注册校验')
@allure.title('测试用例004：密码为空提交注册信息')
def test_case04():
    assert 1==4

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景002，微信用户注册校验')
@allure.title('测试用例005：用户名存在特殊字符')
def test_case05():
    assert 1==5

@allure.feature('测试需求001，用户注册')
@allure.story('测试场景002，微信用户注册校验')
@allure.title('测试用例006：用户名超长提交注册信息')
def test_case06():
    assert 1==6

if __name__ == '__main__':
    pytest.main(['-s',"test_allure.py",'--alluredir','./result'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')