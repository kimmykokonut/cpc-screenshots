import logging
import os
from datetime import datetime

from playwright.sync_api import sync_playwright

from urls import *

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

events_iframe_selector = (
    'iframe[src="https://widgets.sociablekit.com/eventbrite-events/iframe/25357779"]'
)
youtube_iframe_selector = 'iframe[src*="https://www.youtube.com"]'


def wait_for_iframe_load(page, iframe_selector, event_selector, scroll_top=False):
    logger.info(
        f"Waiting for iframe to load...selector={iframe_selector}, event:{event_selector}"
    )
    if scroll_top:
        # scroll top for /learn yt iframe
        page.evaluate("window.scrollTo(0,0)")
    else:
        # Scroll to bottom to trigger events widget loading
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    # wait for iframe to be attached
    page.wait_for_timeout(3000)  # changed from 3k to 5 sec, 5k

    try:
        iframe_element = page.wait_for_selector(
            iframe_selector, timeout=15000, state="attached"
        )
        iframe = iframe_element.content_frame()
        if iframe:
            iframe.wait_for_selector(event_selector, timeout=20000, state="attached")
            page.wait_for_timeout(1000)
        else:
            logger.warning("iframe not found or not loaded.")
    except Exception as e:
        logger.warning(f"Error waiting for iframe or content: {e}")


def take_home_screenshots(page, base_dated_dir, playwright, browser):
    home_dir = os.path.join(base_dated_dir, "home")
    os.makedirs(home_dir, exist_ok=True)

    for url, name in home_urls.items():
        page.set_viewport_size({"width": 1280, "height": 2000})
        page.goto(url)
        logger.info(f"At url: {url}")
        wait_for_iframe_load(page, events_iframe_selector, ".event-single-item")

        # Scroll to page top before screenshot so navbar is in correct location
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(2000)

        page.screenshot(path=f"{home_dir}/{name}.png", full_page=True)
        logger.info(f"Screenshot taken: {name}")

        # take mobile screenshots
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        mobile_page = context.new_page()
        mobile_page.goto(url)
        # wait for events to load
        wait_for_iframe_load(mobile_page, events_iframe_selector, ".event-single-item")
        mobile_page.screenshot(path=f"{home_dir}/{name}-mobile.png", full_page=True)
        mobile_page.close()
        context.close()
        logger.info(f"Mobile screenshot taken: {name}")


def take_content_screenshots(page, base_dated_dir, playwright, browser):
    content_dir = os.path.join(base_dated_dir, "content")
    os.makedirs(content_dir, exist_ok=True)

    for url, name in content_urls.items():
        page.set_viewport_size({"width": 1280, "height": 2000})
        page.goto(url)
        logger.info(f"At url: {url}")
        page.wait_for_load_state("domcontentloaded", timeout=15000)  # change 50k to 15k
        if url == "https://www.capeperpetuacollaborative.org/learn":
            wait_for_iframe_load(
                page,
                youtube_iframe_selector,
                ".ytp-cued-thumbnail-overlay-image",
                scroll_top=True,
            )
        else:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(3000)
        # scroll top
        page.evaluate("window.scrollTo(0, 0)")
        page.screenshot(path=f"{content_dir}/{name}.png", full_page=True)
        logger.info(f"Screenshot taken: {name}")

        # take mobile screenshots
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        mobile_page = context.new_page()
        mobile_page.goto(url)
        # BUG: youtube iframe container not visible in DOM, timed out in mobile emulation
        if url == "https://www.capeperpetuacollaborative.org/learn":
            logger.info("in mobile learn view...")
            wait_for_iframe_load(
                mobile_page,
                youtube_iframe_selector,
                ".ytmCuedOverlayHost",
                scroll_top=True,
            )
        else:
            mobile_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            mobile_page.wait_for_timeout(5000)

        mobile_page.screenshot(path=f"{content_dir}/{name}-mobile.png", full_page=True)
        mobile_page.close()
        context.close()
        logger.info(f"Mobile screenshot taken: {name}")


def take_programs_screenshots(page, base_dated_dir, playwright, browser):
    programs_dir = os.path.join(base_dated_dir, "programs")
    os.makedirs(programs_dir, exist_ok=True)

    for url, name in programs_urls.items():
        page.set_viewport_size({"width": 1280, "height": 2000})
        page.goto(url)
        logger.info(f"At url: {url}")
        page.wait_for_load_state("domcontentloaded", timeout=15000)  # change 50k to 15k
        if url == "https://www.capeperpetuacollaborative.org/land-sea-symposium":
            wait_for_iframe_load(
                page,
                youtube_iframe_selector,
                ".html5-video-container",
                scroll_top=False,
            )
        page.screenshot(path=f"{programs_dir}/{name}.png", full_page=True)
        logger.info(f"Screenshot taken: {name}")
        # take mobile screenshots
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        mobile_page = context.new_page()
        mobile_page.goto(url)
        mobile_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        mobile_page.wait_for_timeout(6000)
        mobile_page.evaluate("window.scrollTo(0, 0)")
        mobile_page.wait_for_timeout(1000)
        mobile_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        mobile_page.wait_for_timeout(3000)
        mobile_page.screenshot(path=f"{programs_dir}/{name}-mobile.png", full_page=True)
        mobile_page.close()
        context.close()
        logger.info(f"Mobile screenshot taken: {name}")


def take_forms_screenshots(page, base_dated_dir, playwright, browser):
    forms_dir = os.path.join(base_dated_dir, "forms")
    os.makedirs(forms_dir, exist_ok=True)

    for url, name in forms_urls.items():
        page.set_viewport_size({"width": 1280, "height": 720})
        page.goto(url)
        logger.info(f"At url: {url}")
        page.wait_for_load_state("domcontentloaded")
        page.screenshot(path=f"{forms_dir}/{name}.png", full_page=True)
        logger.info(f"Screenshot taken: {name}")
        # take mobile screenshots
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        mobile_page = context.new_page()
        mobile_page.goto(url)
        mobile_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        mobile_page.wait_for_timeout(3000)
        mobile_page.screenshot(path=f"{forms_dir}/{name}-mobile.png", full_page=True)
        mobile_page.close()
        context.close()
        logger.info(f"Mobile screenshot taken: {name}")


def main():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    # create dated folder to hold screenshots
    base_dated_dir = f"/screenshots/{timestamp}"
    os.makedirs(base_dated_dir, exist_ok=True)

    logger.info("...............lettuce begin..............")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # take_home_screenshots(page, base_dated_dir, p, browser)
        take_content_screenshots(page, base_dated_dir, p, browser)
        # take_programs_screenshots(page, base_dated_dir, p, browser)
        # take_forms_screenshots(page, base_dated_dir, p, browser)

        browser.close()
        logger.info("------------bye!------------")


if __name__ == "__main__":
    main()
