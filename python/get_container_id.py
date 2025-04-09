import subprocess

def get_container_id(container_name):
    try:
        # Run the docker command to get the container ID
        cmd = ['docker', 'ps', '-f', f'name={container_name}', '-q']
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Get the container ID from the output (strip whitespace)
        container_id = result.stdout.strip()
        
        if container_id:
            print(f"Container ID for '{container_name}': {container_id}")
            return container_id
        else:
            print(f"No running container found with name '{container_name}'")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing docker command: {e}")
        return None
    except FileNotFoundError:
        print("Docker is not installed or not found in PATH")
        return None

# Specify the container name
container_name = "mdlbkp-deb12-moodle"

# Get and store the container ID
container_id = get_container_id(container_name)

# Example: Use the container_id variable
if container_id:
    print(f"Stored Container ID: {container_id}")
else:
    print("Failed to retrieve Container ID")