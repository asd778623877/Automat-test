from appium import webdriver

def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'A02YECPH27MHJ'
    # app的信息com.ecaray.epark.xiangyang com.ecaray.epark.xiangyang.ui.GuideActivity
    desired_caps['appPackage'] = 'com.mobilefly.pda'
    desired_caps['appActivity'] = 'com.mobilefly.pda.activity.LoginActivity'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver