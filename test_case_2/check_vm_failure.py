import subprocess

def get_vm_pod_status(vm_name):
    try:
        # Get the pod name that belongs to the VM instance
        get_pod_cmd = [
            "kubectl", "get", "pods",
            "-l", f"kubevirt.io/domain={vm_name}",
            "-o", "jsonpath={.items[0].status.phase}"
        ]
        result = subprocess.run(get_pod_cmd, capture_output=True, text=True)
        status = result.stdout.strip()
        print(f"Pod for VM '{vm_name}' is in status: {status}")
        return status
    except Exception as e:
        print(f"Error while checking pod status: {e}")
        return None

if __name__ == "__main__":
    get_vm_pod_status("invalid-vm")
