import os
import pytest
from selenium import webdriver
import allure
from common import configpath
@pytest.fixture(scope='function',autouse=True)
def browser():
    # 静默执行
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    global _driver
    _driver = None
    if _driver is None:
        _driver = webdriver.Chrome(chrome_options=option)
        _driver.implicitly_wait(10)
        _driver.get('https://mail.qq.com/')
        _driver.maximize_window()
    yield _driver
    _driver.quit()
    _driver = None

# 钩子函数 添加工作环境 environment.properities
def pytest_sessionfinish():
    r = configpath.ROOT_DIR
    with open(r + "/report/allure-raw/environment.properties", "w") as f:
        f.write("browser=chrome\nautor=wanfeng\ndomain=https://mail.qq.com/")


# allure 失败用例自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)