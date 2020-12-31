# End-to-end deployment example

> This example is a basic example on end-to-end automated deplyment with Ansible and CVP. Way more advanced content can be found in [AVD](https://github.com/aristanetworks/ansible-avd).

This example leverages Ansible and Cloudvision to do an end-to-end deplyment example.
[Ansible modules for Cloudvision](https://github.com/aristanetworks/ansible-cvp) are used.

The starting point is that all leaf switches in the example have no config and are automatically registered in CVP by using ZTP (see [day1 example4](https://github.com/aristaiberia/automation101/tree/main/day1_ztp/example4_cloudvision)).

![Inventory](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example4_cloudvision/images/inventory.png)

So at this point all switches are just registered into CVP and in assigned to the Undefined container as expected.

![undefined](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/undefined.png)

As expected no configlets exist for now other than the default SYS_TelemetryBuilder

![noconfiglets](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/noconfiglets.png)

Once switches are registered in CVP, ansible playbook runs to:

* Create Container hierarchy
* Create Configlets and apply them to corresponding containers and devices
* Move switches from the undefined container to the corresponding container
* Execute tasks that are created in CVP for config changes

First configlets are created (but not assigned no anything yet). Note that containers and devices counters are all zero.

![unassignedconfiglets.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/unassignedconfiglets.png)

Then the container hierarchy is created. Note that devices are still in the undefined container.

![containerhierarchy.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/containerhierarchy.png)

First per-switch configlets are assigned `at device level` and switches moved to the corresponding containers, this creates CVP tasks that are also executed by the playbook

![assignperswitchconfiglets.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/assignperswitchconfiglets.png)

![assignperswitchconfigletstasks.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/assignperswitchconfigletstasks.png)

At this point the switches reboot due to exiting ZTP mode, after that, the rest of configlets are assigned at `container level`. So note that now, all configlets are assigned either at device level or at container level.

![assignedconfiglets.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/assignedconfiglets.png)

In turn, it creates new tasks that are executed as well by the playbook

![tasks.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/tasks.png)

Once it has been completed everything has been setup

![done.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/done.png)

All switches have the expected configuration

![config.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/config.png)

And for instance, if we compare config between switches in different floors, as expected, we see that the per-switch config (hostname and management ip address) and per-floor config (vlans) are different meanwhile the rest is equal.

![configdiff.png](https://github.com/aristaiberia/automation101/blob/main/day3_ansible/example8_e2e/images/configdiff.png)

Here is the output from the Ansible playbook execution:

```
# ansible-playbook e2e.yml 

PLAY [END-TO-END Network Configuration] ******************************************************************************

TASK [CVFACTS] *******************************************************************************************************
Thursday 31 December 2020  13:24:07 +0100 (0:00:00.019)       0:00:00.019 ***** 
ok: [10.34.0.2]

TASK [CREATE GLOBAL CONFIGLETS] **************************************************************************************
Thursday 31 December 2020  13:24:15 +0100 (0:00:07.937)       0:00:07.956 ***** 
ok: [10.34.0.2]

TASK [CREATE LEAVES CONFIGLETS] **************************************************************************************
Thursday 31 December 2020  13:24:17 +0100 (0:00:02.087)       0:00:10.044 ***** 
ok: [10.34.0.2]

TASK [LOAD PER-FLOOR INFO] *******************************************************************************************
Thursday 31 December 2020  13:24:19 +0100 (0:00:01.835)       0:00:11.880 ***** 
ok: [10.34.0.2]

TASK [CREATE PER-FLOOR CONFIGLETS] ***********************************************************************************
Thursday 31 December 2020  13:24:19 +0100 (0:00:00.553)       0:00:12.433 ***** 
ok: [10.34.0.2] => (item={'key': 'floor1_config', 'value': {'floor': '1', 'data_vlan': '101', 'voice_vlan': '102', 'corp_vlan': '103', 'guest_vlan': '104'}})
ok: [10.34.0.2] => (item={'key': 'floor2_config', 'value': {'floor': '2', 'data_vlan': '201', 'voice_vlan': '202', 'corp_vlan': '203', 'guest_vlan': '204'}})
ok: [10.34.0.2] => (item={'key': 'floor3_config', 'value': {'floor': '3', 'data_vlan': '301', 'voice_vlan': '302', 'corp_vlan': '303', 'guest_vlan': '304'}})

TASK [LOAD PER-SWITCH INFO] ******************************************************************************************
Thursday 31 December 2020  13:24:23 +0100 (0:00:04.090)       0:00:16.524 ***** 
ok: [10.34.0.2]

TASK [CREATE PER-SWITCH CONFIGLETS] **********************************************************************************
Thursday 31 December 2020  13:24:24 +0100 (0:00:00.549)       0:00:17.073 ***** 
ok: [10.34.0.2] => (item={'key': '50:54:00:00:11:11', 'value': {'hostname': 'vlab11', 'management_ip': '10.34.0.11/24'}})
ok: [10.34.0.2] => (item={'key': '50:54:00:00:12:12', 'value': {'hostname': 'vlab12', 'management_ip': '10.34.0.12/24'}})
ok: [10.34.0.2] => (item={'key': '50:54:00:00:21:21', 'value': {'hostname': 'vlab21', 'management_ip': '10.34.0.21/24'}})
ok: [10.34.0.2] => (item={'key': '50:54:00:00:22:22', 'value': {'hostname': 'vlab22', 'management_ip': '10.34.0.22/24'}})
ok: [10.34.0.2] => (item={'key': '50:54:00:00:31:31', 'value': {'hostname': 'vlab31', 'management_ip': '10.34.0.31/24'}})
ok: [10.34.0.2] => (item={'key': '50:54:00:00:32:32', 'value': {'hostname': 'vlab32', 'management_ip': '10.34.0.32/24'}})

TASK [LOAD EMPTY CONTAINERS INFO] ************************************************************************************
Thursday 31 December 2020  13:24:32 +0100 (0:00:07.988)       0:00:25.062 ***** 
ok: [10.34.0.2]

TASK [CREATE EMPTY CONTAINERS] ***************************************************************************************
Thursday 31 December 2020  13:24:32 +0100 (0:00:00.530)       0:00:25.593 ***** 
ok: [10.34.0.2]

TASK [REFRESH FACTS] *************************************************************************************************
Thursday 31 December 2020  13:24:47 +0100 (0:00:14.673)       0:00:40.266 ***** 
ok: [10.34.0.2]

TASK [ASSIGN PER-SWITCH CONFIGLET] ***********************************************************************************
Thursday 31 December 2020  13:24:58 +0100 (0:00:11.344)       0:00:51.610 ***** 
changed: [10.34.0.2] => (item={'key': '50:54:00:00:11:11', 'value': {'hostname': 'vlab11', 'management_ip': '10.34.0.11/24'}})
changed: [10.34.0.2] => (item={'key': '50:54:00:00:12:12', 'value': {'hostname': 'vlab12', 'management_ip': '10.34.0.12/24'}})
changed: [10.34.0.2] => (item={'key': '50:54:00:00:21:21', 'value': {'hostname': 'vlab21', 'management_ip': '10.34.0.21/24'}})
changed: [10.34.0.2] => (item={'key': '50:54:00:00:22:22', 'value': {'hostname': 'vlab22', 'management_ip': '10.34.0.22/24'}})
changed: [10.34.0.2] => (item={'key': '50:54:00:00:31:31', 'value': {'hostname': 'vlab31', 'management_ip': '10.34.0.31/24'}})
changed: [10.34.0.2] => (item={'key': '50:54:00:00:32:32', 'value': {'hostname': 'vlab32', 'management_ip': '10.34.0.32/24'}})

TASK [CVFACTS] *******************************************************************************************************
Thursday 31 December 2020  13:25:13 +0100 (0:00:15.032)       0:01:06.643 ***** 
ok: [10.34.0.2]

TASK [RUN TASKS TO ASSIGN PER-SWITCH CONFIG AND MOVE SWITCHES - WAIT FOR RELOAD] *************************************
Thursday 31 December 2020  13:25:26 +0100 (0:00:12.500)       0:01:19.143 ***** 
changed: [10.34.0.2]

TASK [LOAD CONTAINERS INFO] ******************************************************************************************
Thursday 31 December 2020  13:29:12 +0100 (0:03:46.709)       0:05:05.853 ***** 
ok: [10.34.0.2]

TASK [APPLY CONFIGLETS TO CONTAINERS] ********************************************************************************
Thursday 31 December 2020  13:29:13 +0100 (0:00:00.616)       0:05:06.470 ***** 
ok: [10.34.0.2]

TASK [CVP FACTS] *****************************************************************************************************
Thursday 31 December 2020  13:29:24 +0100 (0:00:11.063)       0:05:17.533 ***** 
ok: [10.34.0.2]

TASK [RUN TASKS TO ASSIGN CONFIGLETS TO CONTAINERS] ******************************************************************
Thursday 31 December 2020  13:29:35 +0100 (0:00:10.981)       0:05:28.515 ***** 
changed: [10.34.0.2]

PLAY RECAP ***********************************************************************************************************
10.34.0.2                  : ok=17   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

Thursday 31 December 2020  13:29:45 +0100 (0:00:09.857)       0:05:38.373 ***** 
=============================================================================== 
RUN TASKS TO ASSIGN PER-SWITCH CONFIG AND MOVE SWITCHES - WAIT FOR RELOAD ----------------------------------- 226.71s
ASSIGN PER-SWITCH CONFIGLET ---------------------------------------------------------------------------------- 15.03s
CREATE EMPTY CONTAINERS -------------------------------------------------------------------------------------- 14.67s
CVFACTS ------------------------------------------------------------------------------------------------------ 12.50s
REFRESH FACTS ------------------------------------------------------------------------------------------------ 11.34s
APPLY CONFIGLETS TO CONTAINERS ------------------------------------------------------------------------------- 11.06s
CVP FACTS ---------------------------------------------------------------------------------------------------- 10.98s
RUN TASKS TO ASSIGN CONFIGLETS TO CONTAINERS ------------------------------------------------------------------ 9.86s
CREATE PER-SWITCH CONFIGLETS ---------------------------------------------------------------------------------- 7.99s
CVFACTS ------------------------------------------------------------------------------------------------------- 7.94s
CREATE PER-FLOOR CONFIGLETS ----------------------------------------------------------------------------------- 4.09s
CREATE GLOBAL CONFIGLETS -------------------------------------------------------------------------------------- 2.09s
CREATE LEAVES CONFIGLETS -------------------------------------------------------------------------------------- 1.84s
LOAD CONTAINERS INFO ------------------------------------------------------------------------------------------ 0.62s
LOAD PER-FLOOR INFO ------------------------------------------------------------------------------------------- 0.55s
LOAD PER-SWITCH INFO ------------------------------------------------------------------------------------------ 0.55s
LOAD EMPTY CONTAINERS INFO ------------------------------------------------------------------------------------ 0.53s
ansible-playbook e2e.yml  53.17s user 6.22s system 17% cpu 5:39.49 total
```
