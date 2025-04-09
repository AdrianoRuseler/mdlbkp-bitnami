import subprocess
import os

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

def load_commands_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Commands file '{file_path}' not found")
        return []
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and filter out empty lines
            commands = [line.strip() for line in file if line.strip()]
        return commands
    except Exception as e:
        print(f"Error reading commands file: {e}")
        return []

def run_bash_commands(container_id, working_dir="/opt/bitnami/moodle", commands=None):
    if not container_id:
        print("No Container ID provided. Cannot run commands.")
        return
    
    try:
        if commands:
            # Run predefined list of commands in the specified directory
            for cmd in commands:
                full_cmd = f"cd {working_dir} && {cmd}"
                print(f"Running command in {working_dir}: {cmd}")
                exec_cmd = ['docker', 'exec', '-it', container_id, 'bash', '-c', full_cmd]
                result = subprocess.run(exec_cmd, capture_output=True, text=True)
                print(f"Output:\n{result.stdout}")
                if result.stderr:
                    print(f"Errors:\n{result.stderr}")
        else:
            # Interactive mode: prompt user for commands in the specified directory
            print(f"Enter Bash commands to run in {working_dir} (type 'exit' to stop):")
            while True:
                cmd = input("Command: ")
                if cmd.lower() == 'exit':
                    break
                full_cmd = f"cd {working_dir} && {cmd}"
                exec_cmd = ['docker', 'exec', '-it', container_id, 'bash', '-c', full_cmd]
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

# Load predefined commands from a file
commands_file = "commands.txt"
predefined_commands = load_commands_from_file(commands_file)

# Run commands in /opt/bitnami/moodle (uncomment one of the following)
# Option 1: Run predefined commands from file
if predefined_commands:
    run_bash_commands(container_id, working_dir="/opt/bitnami/moodle", commands=predefined_commands)
else:
    print("No commands loaded from file, switching to interactive mode")

# Option 2: Interactive mode (default if no commands or file not found)
if container_id and not predefined_commands:
    run_bash_commands(container_id, working_dir="/opt/bitnami/moodle")
elif not container_id:
    print("Failed to retrieve Container ID, cannot run commands")