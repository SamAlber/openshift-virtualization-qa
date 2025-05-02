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

---

### ✅ Test Case 3: Live Migration Works Under Normal Conditions

**Objective:** Verify a running VM can be migrated to another node.

**Steps:**
1. Ensure a VM is Running
2. Trigger migration (e.g., using `virtctl migrate`)
3. Monitor pod changes and VM status

**Expected Result:** VM continues running on the new node, with no data loss.
