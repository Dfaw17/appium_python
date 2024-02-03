from selenium.webdriver.common.by import By
from helper.action import *
from pom.pom_demo import *


def test_demo_1(open_driver):
    click_elem(open_driver, close_modal)
    click_elem(open_driver, btn_fab)
    click_elem(open_driver, date1)
    click_elem(open_driver, date2)
    click_elem(open_driver, date3)
    click_elem(open_driver, category1)
    click_elem(open_driver, category2)
    input_text(open_driver, amount, "30000")
    input_text(open_driver, note, "Rokok Surya")
    click_elem(open_driver, btnSave)
    wait(1)
    check_display(open_driver, assertRokokSurya)
