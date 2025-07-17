import requests
import os

from faker import Faker

def generate_env_file(filename='.env'):
    """Generate a .env file with random credentials using Faker."""
    fake = Faker()

    # Generate random values
    mariadb_password = fake.password()
    mariadb_root_password = fake.password()
    moodle_admin_password = fake.password()
    lldap_admin_password = fake.password()
    # Generate a random string that mimics a JWT secret
    jwt_secret = fake.sha256()

    # Content for .env file
    env_content = f"""MARIADB_PASSWORD={mariadb_password}
MARIADB_ROOT_PASSWORD={mariadb_root_password}
MOODLE_PASSWORD={moodle_admin_password}
LLDAP_JWT={jwt_secret}
LLDAP_PASSWORD={lldap_admin_password}
"""

    # Write to .env file
    try:
        with open(filename, 'w') as f:
            f.write(env_content)
        print(f"Successfully created {filename} with random credentials:")
        print("-" * 50)
        print(env_content)
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
        
def download_and_append_github_file(output_filename, github_url=None, content=None):
    """
    Appends content to a file, either by downloading from a GitHub URL or using provided content.
    
    Args:
        output_filename (str): The name of the file to append to
        github_url (str, optional): The GitHub URL to download from
        content (str, optional): Direct content to append (if no URL is provided)
    
    Returns:
        bool: True if successful, False if an error occurred
    """
    try:
        # Validate input: either github_url or content must be provided, but not both
        if (github_url is None and content is None) or (github_url is not None and content is not None):
            raise ValueError("Exactly one of github_url or content must be provided")

        # If github_url is provided, download the content
        if github_url:
            # Ensure the URL is in raw format
            if "github.com" in github_url and "/blob/" in github_url:
                github_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            
            # Download the file from GitHub
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(github_url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            content = response.text
            source_info = f"Content from {github_url}"
        else:
            # Use the provided content directly
            source_info = "Directly provided content"

        # Prepare the separator (to clearly mark new content)
        separator = "=" * 50
        
        # Prepare the header for this entry
        #header = f"\n{separator}\n{source_info}\n{separator}\n"
        
        # Prepare the full content to append
        #full_content = header + content + "\n"  # Ensure final newline
        full_content = content + "\n"  # Ensure final newline
        
        # Append the content at the end of the local file
        with open(output_filename, 'a', encoding='utf-8') as file:
            # If file is not empty, ensure we're starting on a new line
            if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
                file.write("\n")  # Add extra newline before new content
            file.write(full_content)
        
        print(f"Successfully appended {'downloaded ' if github_url else ''}content to the end of {output_filename}")
        return True
    
    except requests.RequestException as e:
        print(f"Error downloading the GitHub file: {e}")
        return False
    except IOError as e:
        print(f"Error writing to the local file: {e}")
        return False
    except ValueError as e:
        print(f"Input error: {e}")
        return False

def display_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print("\nCurrent file contents:")
            print(file.read())
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

def read_env_file_manual(filename='.env'):
    """Manually read and parse the .env file without dependencies."""
    env_vars = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Skip empty lines or comments
                line = line.strip()
                if line and not line.startswith('#'):
                    # Split on the first '=' only
                    if '=' in line:
                        key, value = line.split('=', 1)
                        env_vars[key] = value
        
        # Print the variables
        print(f"Successfully read {filename}:")
        print("-" * 50)
        for key, value in env_vars.items():
            print(f"{key}={value}")
        
        return env_vars
    
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None
        
if __name__ == "__main__":    
    generate_env_file()
    env_vars = read_env_file_manual()
    if env_vars:
        # Example: Access a specific variable
        print("\nExample usage:")
        print(f"Moodle admin password: {env_vars['MOODLE_PASSWORD']}")
        
        # Example usage
        output_filename = "defaults-dist.php"
        
        # Example 1: Downloading from GitHub URL
        github_url = "https://raw.githubusercontent.com/AdrianoRuseler/mdlbkp-bitnami/refs/heads/main/docker/defaults-dist.php"
        print(f"\nProcessing GitHub URL: {github_url}")
        download_and_append_github_file(output_filename, github_url=github_url)
        
        # Example 2: Appending direct content
        direct_content = f"""$defaults['moodle']['auth_instructions'] = 'MOODLE_USERNAME: admin
        MOODLE_PASSWORD: {env_vars['MOODLE_PASSWORD']}';
        """ 
        print(f"\nAppending direct content")
        download_and_append_github_file(output_filename, content=direct_content)
        
        # Display the final file contents
        display_file_contents(output_filename)
    