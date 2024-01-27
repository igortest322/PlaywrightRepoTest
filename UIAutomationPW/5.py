from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    
    page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("coding_qual_input.txt")
    page.get_by_role("button", name="Upload").click()
    page.get_by_role("heading", name="File Uploaded!").click()
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="coding_qual_input.txt").click()
    #download = download_info.value

    # ---------------------
    context.close()
    browser.close()
print("Passed")

with sync_playwright() as playwright:
    run(playwright)