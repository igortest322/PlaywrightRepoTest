from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state('networkidle')
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("2")
    page.locator("#dropdown").select_option("1")
    page.wait_for_load_state('networkidle')
    expect(page.locator("#dropdown").select_option("selected"))
    

    # ---------------------
    context.close()
    browser.close()
print("Passed")

with sync_playwright() as playwright:
    run(playwright)