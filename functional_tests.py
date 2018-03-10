from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a new online to-do app.
        # She goes check out the homepage

        self.browser.get('http://localhost:8000')

        # She notices the page title and header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # There is still a text box inviting her to add another item.
        # She ads "use peacock feathers to make a fly"

        # The page updates and shows both items on her list

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list.
        # She sees that the site has generate a unique URL for her
        self.fail('Finish the test!')
        # She visists that URL - her to-do list is still there!

        # She goes happily back to sleep


if __name__ == '__main__':
    unittest.main()
