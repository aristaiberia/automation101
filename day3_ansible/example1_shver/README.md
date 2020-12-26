# show version example

This example uses the [eos_command](https://docs.ansible.com/ansible/2.9/modules/eos_command_module.html) Ansible module to show the hostname and version running on EOS switches.

```
# ansible-playbook -i hosts showversion.yml 

PLAY [all] *********************************************************************************************

TASK [get eos version and hostname] ********************************************************************
ok: [10.34.0.101]
ok: [10.34.0.21]
ok: [10.34.0.11]
ok: [10.34.0.12]
ok: [10.34.0.102]
ok: [10.34.0.22]
ok: [10.34.0.31]
ok: [10.34.0.32]

TASK [debugs] ******************************************************************************************
ok: [10.34.0.12] => {
    "msg": "Switch vlab12 runs EOS version 4.24.0F"
}
ok: [10.34.0.101] => {
    "msg": "Switch vlab01 runs EOS version 4.22.3M"
}
ok: [10.34.0.21] => {
    "msg": "Switch vlab21 runs EOS version 4.24.0F"
}
ok: [10.34.0.102] => {
    "msg": "Switch vlab02 runs EOS version 4.22.3M"
}
ok: [10.34.0.11] => {
    "msg": "Switch vlab11 runs EOS version 4.24.0F"
}
ok: [10.34.0.31] => {
    "msg": "Switch vlab31 runs EOS version 4.24.0F"
}
ok: [10.34.0.22] => {
    "msg": "Switch vlab22 runs EOS version 4.24.0F"
}
ok: [10.34.0.32] => {
    "msg": "Switch vlab32 runs EOS version 4.24.0F"
}

PLAY RECAP *********************************************************************************************
10.34.0.101                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook -i hosts showversion.yml  11.21s user 3.13s system 115% cpu 12.465 total
```

By using `--limit` you can limit the devices or groups over which the playbook will act.

```
# ansible-playbook --limit floor2 -i hosts showversion.yml

PLAY [all] ********************************************************************************************************************************

TASK [get eos version and hostname] *******************************************************************************************************
ok: [10.34.0.21]
ok: [10.34.0.22]

TASK [debugs] *****************************************************************************************************************************
ok: [10.34.0.21] => {
    "msg": "Switch vlab21 runs EOS version 4.24.0F"
}
ok: [10.34.0.22] => {
    "msg": "Switch vlab22 runs EOS version 4.24.0F"
}

PLAY RECAP ********************************************************************************************************************************
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

# ansible-playbook --limit 10.34.0.31 -i hosts showversion.yml

PLAY [all] ********************************************************************************************************************************

TASK [get eos version and hostname] *******************************************************************************************************
ok: [10.34.0.31]

TASK [debugs] *****************************************************************************************************************************
ok: [10.34.0.31] => {
    "msg": "Switch vlab31 runs EOS version 4.24.0F"
}

PLAY RECAP ********************************************************************************************************************************
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
