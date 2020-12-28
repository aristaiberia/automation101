# Collecting Facts example

## EOS Facts

This example uses the [eos_facts](https://docs.ansible.com/ansible/2.9/modules/eos_facts_module.html) Ansible module to collect EOS facts. In particular this example collects interfaces and vlans information. Note that `gather_subset` is deprecated, instead `gather_network_resources` is easier to later combine with eos resource modules.

```
# ansible-playbook facts.yml 

PLAY [all] *************************************************************************

TASK [gather facts] ****************************************************************
[WARNING]: default value for `gather_subset` will be changed to `min` from
`!config` v2.11 onwards
ok: [10.34.0.12]
ok: [10.34.0.11]
ok: [10.34.0.101]
ok: [10.34.0.21]
ok: [10.34.0.102]
ok: [10.34.0.31]
ok: [10.34.0.32]
ok: [10.34.0.22]

TASK [debugs] **********************************************************************
ok: [10.34.0.101] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "interfaces",
                "vlans"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Port-Channel10"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel11"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel12"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel21"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel22"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel31"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel32"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet6"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet7"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet8"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan101"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan301"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan4094"
                    }
                ],
                "vlans": [
                    {
                        "state": "active",
                        "vlan_id": 101
                    },
                    {
                        "state": "active",
                        "vlan_id": 102
                    },
                    {
                        "state": "active",
                        "vlan_id": 103
                    },
                    {
                        "state": "active",
                        "vlan_id": 104
                    },
                    {
                        "state": "active",
                        "vlan_id": 201
                    },
                    {
                        "state": "active",
                        "vlan_id": 202
                    },
                    {
                        "state": "active",
                        "vlan_id": 203
                    },
                    {
                        "state": "active",
                        "vlan_id": 204
                    },
                    {
                        "state": "active",
                        "vlan_id": 301
                    },
                    {
                        "state": "active",
                        "vlan_id": 302
                    },
                    {
                        "state": "active",
                        "vlan_id": 303
                    },
                    {
                        "state": "active",
                        "vlan_id": 304
                    },
                    {
                        "state": "active",
                        "vlan_id": 4094
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.11] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "interfaces",
                "vlans"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "1_floor_data",
                        "state": "active",
                        "vlan_id": 101
                    },
                    {
                        "name": "1_floor_voice",
                        "state": "active",
                        "vlan_id": 102
                    },
                    {
                        "name": "1_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 103
                    },
                    {
                        "name": "1_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 104
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.102] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "interfaces",
                "vlans"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Port-Channel10"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel11"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel12"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel21"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel22"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel31"
                    },
                    {
                        "enabled": true,
                        "name": "Port-Channel32"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet6"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet7"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet8"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan101"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan301"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan4094"
                    }
                ],
                "vlans": [
                    {
                        "state": "active",
                        "vlan_id": 101
                    },
                    {
                        "state": "active",
                        "vlan_id": 102
                    },
                    {
                        "state": "active",
                        "vlan_id": 103
                    },
                    {
                        "state": "active",
                        "vlan_id": 104
                    },
                    {
                        "state": "active",
                        "vlan_id": 201
                    },
                    {
                        "state": "active",
                        "vlan_id": 202
                    },
                    {
                        "state": "active",
                        "vlan_id": 203
                    },
                    {
                        "state": "active",
                        "vlan_id": 204
                    },
                    {
                        "state": "active",
                        "vlan_id": 301
                    },
                    {
                        "state": "active",
                        "vlan_id": 302
                    },
                    {
                        "state": "active",
                        "vlan_id": 303
                    },
                    {
                        "state": "active",
                        "vlan_id": 304
                    },
                    {
                        "state": "active",
                        "vlan_id": 4094
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.12] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "vlans",
                "interfaces"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "1_floor_data",
                        "state": "active",
                        "vlan_id": 101
                    },
                    {
                        "name": "1_floor_voice",
                        "state": "active",
                        "vlan_id": 102
                    },
                    {
                        "name": "1_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 103
                    },
                    {
                        "name": "1_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 104
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.21] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "vlans",
                "interfaces"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "2_floor_data",
                        "state": "active",
                        "vlan_id": 201
                    },
                    {
                        "name": "2_floor_voice",
                        "state": "active",
                        "vlan_id": 202
                    },
                    {
                        "name": "2_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 203
                    },
                    {
                        "name": "2_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 204
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.22] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "vlans",
                "interfaces"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "2_floor_data",
                        "state": "active",
                        "vlan_id": 201
                    },
                    {
                        "name": "2_floor_voice",
                        "state": "active",
                        "vlan_id": 202
                    },
                    {
                        "name": "2_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 203
                    },
                    {
                        "name": "2_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 204
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.31] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "vlans",
                "interfaces"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "3_floor_data",
                        "state": "active",
                        "vlan_id": 301
                    },
                    {
                        "name": "3_floor_voice",
                        "state": "active",
                        "vlan_id": 302
                    },
                    {
                        "name": "3_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 303
                    },
                    {
                        "name": "3_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 304
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}
ok: [10.34.0.32] => {
    "output": {
        "ansible_facts": {
            "ansible_net_gather_network_resources": [
                "interfaces",
                "vlans"
            ],
            "ansible_net_gather_subset": [],
            "ansible_network_resources": {
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Ethernet1"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet2"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet3"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Ethernet5"
                    },
                    {
                        "enabled": true,
                        "name": "Management1"
                    }
                ],
                "vlans": [
                    {
                        "name": "3_floor_data",
                        "state": "active",
                        "vlan_id": 301
                    },
                    {
                        "name": "3_floor_voice",
                        "state": "active",
                        "vlan_id": 302
                    },
                    {
                        "name": "3_floor_corp_ssid",
                        "state": "active",
                        "vlan_id": 303
                    },
                    {
                        "name": "3_floor_guest_ssid",
                        "state": "active",
                        "vlan_id": 304
                    }
                ]
            }
        },
        "changed": false,
        "failed": false,
        "warnings": [
            "default value for `gather_subset` will be changed to `min` from `!config` v2.11 onwards"
        ]
    }
}

PLAY RECAP *************************************************************************
10.34.0.101                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook facts.yml  12.00s user 2.56s system 112% cpu 12.911 total
```
