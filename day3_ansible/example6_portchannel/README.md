# Portchannel example

This example uses the EOS resources modules (`eos_lag_interfaces`, `eos_l2_interfaces`) as well as `eos_config` module to configure a Portchannel and trunk some vlans. The vlans that are trunked for each switch are defined in the `inventory file`.

```
# ansible-playbook po.yml 

PLAY [all] ********************************************************************************************************

TASK [setup po12] *************************************************************************************************
changed: [10.34.0.31]
changed: [10.34.0.11]
changed: [10.34.0.21]
changed: [10.34.0.22]
changed: [10.34.0.12]
changed: [10.34.0.32]

TASK [allowed vlans] **********************************************************************************************
changed: [10.34.0.12]
changed: [10.34.0.21]
changed: [10.34.0.11]
changed: [10.34.0.31]
changed: [10.34.0.22]
changed: [10.34.0.32]

TASK [trunk po12] *************************************************************************************************
changed: [10.34.0.12]
changed: [10.34.0.22]
changed: [10.34.0.21]
changed: [10.34.0.11]
changed: [10.34.0.31]
changed: [10.34.0.32]

PLAY RECAP ********************************************************************************************************
10.34.0.11                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook po.yml  14.81s user 3.42s system 76% cpu 23.723 total
```

Once the playbook has run, this is what the switch looks like

```
vlab31#show port-channel active-ports 
Port Channel Port-Channel12:
  Active Ports: Ethernet2 Ethernet1 
vlab31#
vlab31#show port-channel detailed 
Port Channel Port-Channel12
  Active Ports:
       Port            Time became active       Protocol    Mode   
    --------------- ------------------------ -------------- ------ 
       Ethernet1       17:50:39                 LACP        Active 
       Ethernet2       17:50:39                 LACP        Active 

vlab31#show lacp aggregates 
Port Channel Port-Channel12:
 Aggregate ID: [(8000,50-54-00-00-31-31,000C,0000,0000),(8000,52-54-00-00-01-01,001F,0000,0000)]
  Bundled Ports: Ethernet1 Ethernet2 
vlab31#
vlab31#show interfaces trunk 
Port            Mode            Status          Native vlan
Po12            trunk           trunking        1

Port            Vlans allowed
Po12            301-304

Port            Vlans allowed and active in management domain
Po12            None

Port            Vlans in spanning tree forwarding state
Po12            None
```
