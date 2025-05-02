# OpenShift Virtualization QA Sample

This mini-project contains basic test case examples and a Python script used to validate VM functionality in a Kubernetes cluster with KubeVirt installed.

🧪 Goals:
- Understand QA mindset for testing virtualization features
- Test automation using Python
- Practice test design around KubeVirt-powered VMs

# Test Cases - OpenShift Virtualization

---

### ✅ Test Case 1: VM Starts Successfully

**Objective:** Validate that a VirtualMachine resource enters a Running state.

**Steps:**
1. Apply basic `VirtualMachine` YAML
2. Run `kubectl get vm`
3. Confirm the status is `Running`

**Expected Result:** VM shows `Running` in the status field.

---

### ✅ Test Case 2: Invalid Image Causes Failure

**Objective:** Verify system behavior when an invalid containerDisk image is provided.

**Steps:**
1. Apply a `VirtualMachine` with an incorrect image reference
2. Run `kubectl get pod`
3. Observe failure in pod status

**Expected Result:** Pod fails to start, logs show image pull error.