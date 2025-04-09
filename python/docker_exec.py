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

def run_bash_commands(container_id, commands=None):
    if not container_id:
        print("No Container ID provided. Cannot run commands.")
        return
    
    try:
        if commands:
            # Run predefined list of commands
            for cmd in commands:
                print(f"Running command: {cmd}")
                exec_cmd = ['docker', 'exec', '-it', container_id, 'bash', '-c', cmd]
                result = subprocess.run(exec_cmd, capture_output=True, text=True)
                print(f"Output:\n{result.stdout}")
                if result.stderr:
                    print(f"Errors:\n{result.stderr}")
        else:
            # Interactive mode: prompt user for commands
            print("Enter Bash commands to run in the container (type 'exit' to stop):")
            while True:
                cmd = input("Command: ")
                if cmd.lower() == 'exit':
                    break
                exec_cmd = ['docker', 'exec', '-it', container_id, 'bash', '-c', cmd]
                result = subprocess.run(exec_cmd, capture_output=True, text=True)
                print(f"Output:\n{result.stdout}")
                if result.stderr:
                    print(f"Errors:\n{result.stderr}")
                    
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
    except FileNotFoundError:
        print("Docker is not installed or not found in PATH")

# Specify the container name
container_name = "mdlbkp-deb12-moodle"

# Get the container ID
container_id = get_container_id(container_name)

# Example: Predefined list of commands (optional)
predefined_commands = [
    "ls -la",  # Replace with valid bash commands for your container
    "whoami",
    "echo $PATH"
]

# Run commands (uncomment one of the following based on your preference)
# Option 1: Run predefined commands
run_bash_commands(container_id, predefined_commands)

# Option 2: Interactive mode (default)
if container_id:
    run_bash_commands(container_id)
else:
    print("Failed to retrieve Container ID, cannot run commands")