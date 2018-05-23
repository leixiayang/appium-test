# -*- coding: utf-8 -*-

import pytest
from appium import webdriver
from base.action import ElementActions
from utils.environment import Environment


@pytest.fixture()
def action():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'app': env.apk,
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,
                    'appPackage': env.app_package,
                    'automationName': 'UIAutomator2',
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()


@pytest.fixture(scope="module")
def action2():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'app': env.apk,
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,
                    'appPackage': env.app_package,
                    'automationName': 'UIAutomator2',
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()
