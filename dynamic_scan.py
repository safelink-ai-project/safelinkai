def dynamic_scan(url):
    data = {
        "title": None,
        "forms": 0,
        "password_fields": 0,
        "scripts": 0
    }

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            page = browser.new_page()
            page.goto(url, timeout=10000)
            page.wait_for_load_state("domcontentloaded")

            data["title"] = page.title()
            data["forms"] = page.locator("form").count()
            data["password_fields"] = page.locator("input[type=password]").count()
            data["scripts"] = page.locator("script").count()

            browser.close()
    except Exception as e:
        data["error"] = "Page failed to load"
        data["details"] = str(e)

    return data
