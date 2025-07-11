# playwright_poc

# Pytest
You can trigger test discovery at any time using the "Test: Refresh Tests" command from the Command Palette.

# Locators
You can build a locator and to find a specific element at any guiven time, even if the element does not exist in the current DOM. For example:
element = page.locator("yld-tag-host-campaign")

This won't generate an exception. The element variable will exist and, once we get into the test where this element might be visible or not, we just have to expect something and then, it will generate an exception