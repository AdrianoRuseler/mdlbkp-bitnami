import csv
import os

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

def main():
    # Example usage
    file_path = 'credentials.csv'  # Replace with your CSV file path
    target_username = 'E02'  # The username to search for
    
    credentials = read_credentials(file_path)
    
    if not credentials:
        print("No credentials were read from the file.")
        return

    # Get specific user's credentials
    user_cred = get_user_credentials(credentials, target_username)
    
    if user_cred:
        print(f"Found credentials for {target_username}:")
        print(f"Username: {user_cred['username']}, Password: {user_cred['password']}")
    else:
        print(f"No credentials found for username: {target_username}")

if __name__ == "__main__":
    main()