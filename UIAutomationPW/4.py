from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("123")
    page.get_by_role("button", name=" Login").click()
    page.get_by_text("Your password is invalid! ×").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
    page.get_by_text("You logged into a secure area").click()
    page.get_by_role("link", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()
print("Passed")

with sync_playwright() as playwright:
    run(playwright)