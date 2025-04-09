
import csv
import os
# First, make sure to install playwright:
# pip install playwright
# playwright install
baseurl="http://localhost"
#navegador="chromium"
navegador="firefox"
#navegador="webkit"

file_path = 'credentials.csv'  # Replace with your CSV file path
target_username = 'e01'  # The username to search for
    
# Synchronous version
from playwright.sync_api import sync_playwright

def read_credentials(file_path):
    """
    Reads usernames and passwords from a CSV file.
    Assumes CSV has headers: 'username' and 'password'
    """
    credentials = []
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return credentials

        # Open and read the CSV file
        with open(file_path, 'r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.DictReader(csvfile)
            
            # Verify required headers are present
            required_headers = {'username', 'password'}
            if not required_headers.issubset(reader.fieldnames):
                print("Error: CSV file must contain 'username' and 'password' headers")
                return credentials

            # Read each row and store credentials
            for row in reader:
                credentials.append({
                    'username': row['username'].strip(),
                    'password': row['password'].strip()
                })
            
        return credentials

    except PermissionError:
        print(f"Error: Permission denied to access '{file_path}'")
        return []
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def get_user_credentials(credentials, target_username):
    """
    Retrieves credentials for a specific username.
    Returns None if user is not found.
    """
    for cred in credentials:
        if cred['username'].lower() == target_username.lower():  # Case-insensitive comparison
            return cred
    return None



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
            #print(f"Username: {user}, Password: {password}")
            page.fill("[placeholder=\"Username\"]", user)
            page.fill("[placeholder=\"Password\"]", password)
            page.click("button:has-text(\"Log in\")")
    
            print("Successfully logged in!")
            
            page.goto(baseurl+"/my/courses.php")
            
            # Keep the browser open until you press Enter in the terminal
            print("Browser will remain open. Press Enter in the terminal to close...")
            input()  # Waits for user input
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":  
        # Example usage
    
    credentials = read_credentials(file_path)
    
    if not credentials:
        print("No credentials were read from the file.")

    # Get specific user's credentials
    user_cred = get_user_credentials(credentials, target_username)
    
    if user_cred:
        print(f"Found credentials for {target_username}:")
        print(f"Username: {user_cred['username']}, Password: {user_cred['password']}")
        # Extract both username and password
        user = user_cred['username']
        password = user_cred['password']
    else:
        print(f"No credentials found for username: {target_username}")
        
    # Run synchronous version
    print("Running synchronous version with "+navegador+"...")
    open_webpage_sync()
    