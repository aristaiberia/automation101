# Config example

This example uses the [eos_config](https://docs.ansible.com/ansible/2.9/modules/eos_config_module.html) Ansible module to configure EOS switches. The configuration is rendered from a Config template (`config.j2` in the example). Variable values to render the template are defined in the `hosts` inventory file (some are global, other are per-group and other per-device).

First note that, if you want, you can see what the module is going to do before touching any switch configuration by using `--check` and `--diff`.

```
# ansible-playbook --limit 10.34.0.31 --check --diff eos_config.yaml

PLAY [all] ********************************************************************************************************************************

TASK [push config based on template] ******************************************************************************************************
--- system:/running-config
+++ session:/ansible_1608983509-session-config
@@ -2,15 +2,32 @@
 !
 ! boot system flash:/vEOS-lab-4.24.0F.swi
 !
+alias sip show ip interface brief
+!
 transceiver qsfp default-mode 4x10G
 !
+logging host 10.34.0.254 514
+!
 hostname vlab31
+ip name-server vrf default 10.34.0.254
 !
 spanning-tree mode mstp
 !
 no aaa root
 !
 username admin privilege 15 role network-admin secret sha512 $6$zg05nuSqCeznzinp$AAMXHmxyacZ0qFxKtsSTLnssLMD8zt29KvBg558jrgPULPfe9WrwfaU07EeWQrw22ud.h5S8e5cR0XwWwZyec0
+!
+vlan 301
+   name 3_floor_data
+!
+vlan 302
+   name 3_floor_voice
+!
+vlan 303
+   name 3_floor_corp_ssid
+!
+vlan 304
+   name 3_floor_guest_ssid
 !
 interface Ethernet1
 !
@@ -29,4 +46,7 @@
 !
 ip route 0.0.0.0/0 10.34.0.1
 !
+management api http-commands
+   no shutdown
+!
 end
[WARNING]: Skipping command `copy running-config startup-config` due to check_mode.  Configuration not copied to non-volatile storage
changed: [10.34.0.31]

PLAY RECAP ********************************************************************************************************************************
10.34.0.31                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

To appy the configurations just run the playbook, for instance:

```
# ansible-playbook --limit leaves eos_config.yaml

PLAY [all] ********************************************************************************************************************************

TASK [push config based on template] ******************************************************************************************************
changed: [10.34.0.22]
changed: [10.34.0.21]
changed: [10.34.0.11]
changed: [10.34.0.12]
changed: [10.34.0.31]
changed: [10.34.0.32]

PLAY RECAP ********************************************************************************************************************************
10.34.0.11                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --limit leaves eos_config.yaml  6.11s user 1.67s system 57% cpu 13.612 total
```
