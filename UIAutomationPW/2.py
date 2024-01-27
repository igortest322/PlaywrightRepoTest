from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    #add action for check Status
    page.get_by_role("checkbox").nth(1).check()
    page.get_by_role("checkbox").nth(1).uncheck()
    page.get_by_role("checkbox").first.check()
    page.get_by_role("checkbox").first.uncheck()

    
    # ---------------------
    context.close()
    browser.close()
print("Passed")

with sync_playwright() as playwright:
    run(playwright)