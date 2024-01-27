from playwright.sync_api import Playwright, sync_playwright, expect
#import pytest
from contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    serch_page = ContactUsPage(page)
    serch_page.navigate()
    serch_page.test_submite_form("Symon", "123 Main", "test@email.com", "123-432-5434", "test subject", "test message haha")
    
    
with sync_playwright() as playwright:
    test_submit_form(playwright)
    
print("Passed")
