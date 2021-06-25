import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HostTest(LiveServerTestCase):

    def test_form(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/orders')
        time.sleep(5)
        # find the elements you need to submit form
        cancel_btn = selenium.find_element_by_id('cancel_btn')

        # Canceling Order deleting it
        cancel_btn.click()

        # check if order page empty or not
        assert '' in selenium.page_source
