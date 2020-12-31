# End-to-end deployment example

> This example is a basic example on end-to-end automated deplyment with Ansible and CVP. Way more advanced content can be found in [AVD](https://github.com/aristanetworks/ansible-avd).

This example leverages Ansible and Cloudvision to do an end-to-end deplyment example.
[Ansible modules for Cloudvision](https://github.com/aristanetworks/ansible-cvp) are used.

The starting point is that all leaf switches in the example have no config and are automatically registered in CVP by using ZTP (see [day1 example4](https://github.com/aristaiberia/automation101/tree/main/day1_ztp/example4_cloudvision)).

![Inventory](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example4_cloudvision/images/inventory.png)

Once switches are registered in CVP, ansible playbook runs to:

* Create Container hierarchy
* Create Configlets and apply them to corresponding containers and devices
* Move switches from the undefined container to the corresponding container
* Execute tasks that are created in CVP for config changes


