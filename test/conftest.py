from helper.config import *
from appium import webdriver
import pytest
import time


@pytest.fixture()
def open_driver():
    caps = {
        "platformName": "Android",
        "appium:udid": my_udid,
        "appium:appActivity": appActivity,
        "appium:appPackage": appPackage,
        "appium:automationName": "uiautomator2",
        "autoGrantPermissions": True,
        "appium:noReset": False,
        "appium:ignoreHiddenApiPolicyError": True,
        "appium:disableAnimations": True,
        "appium:disableIdLocatorAutocompletion": True,
    }
    direct = True
    driver = webdriver.Remote(appium_url, caps, direct_connection=direct)
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.implicitly_wait(3)
    time.sleep(2)
    yield
    open_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE

    yield
    # AFTER SUITE
