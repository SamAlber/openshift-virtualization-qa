import subprocess # Built-in Python module for running shell commands

def check_vm_status(vm_name):
    result = subprocess.run(
        ["kubectl", "get", "vm", vm_name, "-o", "jsonpath={.status.phase}"],
        capture_output=True, # # Capture stdout/stderr so we can print it
        text=True # Return the output as a string, not bytes 
    )
    status = result.stdout.strip() # # Remove leading/trailing whitespace
    print(f"VM '{vm_name}' is in state: {status}")
    return status

if __name__ == "__main__": # If this script is run directly (not imported), run the function below 
    check_vm_status("test-vm") # Call the function with a hardcoded VM name
