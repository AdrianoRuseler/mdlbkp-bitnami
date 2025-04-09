# First, make sure to install playwright:
# pip install playwright
# playwright install
baseurl="http://localhost"
#navegador="chromium"
navegador="firefox"
#navegador="webkit"
user="a1"
password="+v54zPBz8^"

# Synchronous version
from playwright.sync_api import sync_playwright

def open_webpage_sync():
    try:
        with sync_playwright() as p:
            # Launch browser (firefox is used here, but you can use firefox or webkit too)
            if navegador=="chromium":
                browser = p.chromium.launch(headless=False)
            elif navegador=="firefox":
                browser = p.firefox.launch(headless=False)
            elif navegador=="webkit":
                browser = p.webkit.launch(headless=False)
            else:
                browser = p.chromium.launch(headless=False)
                
            # You can adjust these dimensions as needed
            context = browser.new_context(
                viewport=None,  # None allows the browser to use maximized window size
                no_viewport=True  # Ensures viewport matches window size
            )
            # Create a new page
            page = context.new_page()
            # Navigate to the URL
            page.goto(baseurl+"/login/index.php")
            
            # Go to login page
            page.fill("[placeholder=\"Username\"]", user)
            page.fill("[placeholder=\"Password\"]", password)
            page.click("button:has-text(\"Log in\")")
    
            print("Successfully logged in!")
            
            page.goto(baseurl+"/admin/search.php")
            
            # Keep the browser open until you press Enter in the terminal
            print("Browser will remain open. Press Enter in the terminal to close...")
            input()  # Waits for user input
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":  
    # Run synchronous version
    print("Running synchronous version with "+navegador+"...")
    open_webpage_sync()
    