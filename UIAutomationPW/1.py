from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/%22")
    page.get_by_role("button", name="Add Element").click()
    page.get_by_role("button", name="Delete").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Elemental Selenium").click()
    page1 = page1_info.value
    page1.close()

    
    # ---------------------
    context.close()
    browser.close()
print("Passed")

with sync_playwright() as playwright:
    run(playwright)
