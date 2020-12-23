from time import sleep
from appium import webdriver
from common import swipe

desired_caps ={
'deviceName':'M2004J7AC',
'appPackage':'com.tencent.mm',
'appActivity':'.ui.LauncherUI',
'platformName':'Android',
'platformVersion':'10',
'resetKeyboard': True,
'unicodeKeyboard': True,
'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'},
'automationName': 'UiAutomator2',
'noReset': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
ac = driver.current_activity
print(ac)
driver.wait_activity(ac,1000)
swipe.swipeDown(driver,n=3)
driver.find_elements_by_id('com.tencent.mm:id/cna')[0].click()
print (driver.contexts)
ac1 = driver.current_activity
print(ac1)
driver.wait_activity(ac1,1000)
driver.tap([(1020,450)],400)
print('成功点击了')
sleep(10)
driver.close_app()
driver.quit()

