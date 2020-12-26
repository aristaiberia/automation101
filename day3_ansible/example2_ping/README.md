# ping example

This example uses the [eos_command](https://docs.ansible.com/ansible/2.9/modules/eos_command_module.html) Ansible module to ping a given ip address in a given vrf.

```
# ansible-playbook --extra-vars "vrf=default ip=8.8.8.8" ping.yml

PLAY [all] ********************************************************************************************************************************

TASK [ping host] **************************************************************************************************************************
ok: [10.34.0.101]
ok: [10.34.0.102]
ok: [10.34.0.12]
ok: [10.34.0.21]
ok: [10.34.0.11]
ok: [10.34.0.22]
ok: [10.34.0.32]
ok: [10.34.0.31]

PLAY RECAP ********************************************************************************************************************************
10.34.0.101                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --extra-vars "vrf=default ip=8.8.8.8" ping.yml  7.24s user 1.92s system 102% cpu 8.916 total
```

This example also uses `failed_when` to show an example on how you can define conditions for handling errors. For instance, if 10.34.0.31 is not able to reach the given IP address to ping (i.e. 8.8.8.8) this is what you will see.

```
# ansible-playbook --extra-vars "vrf=default ip=8.8.8.8" ping.yml

PLAY [all] ********************************************************************************************************************************

TASK [ping host] **************************************************************************************************************************
ok: [10.34.0.12]
ok: [10.34.0.101]
ok: [10.34.0.21]
ok: [10.34.0.102]
ok: [10.34.0.11]
ok: [10.34.0.22]
ok: [10.34.0.32]
fatal: [10.34.0.31]: FAILED! => {"changed": false, "failed_when_result": true, "stdout": ["PING 8.8.8.8 (8.8.8.8) 72(100) bytes of data.\n\n--- 8.8.8.8 ping statistics ---\n5 packets transmitted, 0 received, 100% packet loss, time 40ms"], "stdout_lines": [["PING 8.8.8.8 (8.8.8.8) 72(100) bytes of data.", "", "--- 8.8.8.8 ping statistics ---", "5 packets transmitted, 0 received, 100% packet loss, time 40ms"]]}

PLAY RECAP ********************************************************************************************************************************
10.34.0.101                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --extra-vars "vrf=default ip=8.8.8.8" ping.yml  8.41s user 1.92s system 89% cpu 11.551 total
```
