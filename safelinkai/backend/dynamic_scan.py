def dynamic_scan(url):

    data = {
        "title": None,
        "forms": 0,
        "password_fields": 0,
        "scripts": 0
    }

    try:
        from playwright.sync_api import sync_playwright  # ✅ moved inside

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=20000)

            data["title"] = page.title()
            data["forms"] = page.locator("form").count()
            data["password_fields"] = page.locator("input[type=password]").count()
            data["scripts"] = page.locator("script").count()

            page.screenshot(path="scan.png")

            browser.close()

    except Exception as e:
        data["error"] = "Page failed to load"
        data["details"] = str(e)  # 🔥 add this for debugging

    return data
