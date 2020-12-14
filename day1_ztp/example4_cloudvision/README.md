# ZTP Cloudvision

This example just shows how easy it is to bind the switches to Cloudvision. Note that this example just registers the switch in Cloudvision and does not push any config to the switch (that will be seen in day3 examples)

In this example the flow is:
1. Switches in ZTP mode make DHCP requests
2. DHCP server running the provided configuration (dhcp.conf.lab4) serves the same Bootfilename URL to all switches pointing to a URL directly served by Cloudvision (ztp/bootstrap). Please note that no per-switch dhcp settings are required at all, the ones provided in the dhcp configuration in this example are just for convenience to later see matching switch IPs with SystemMACs. 
3. The switch downloads the script and executes it. There is no prior configuration done in Cloudvision. Cloudvision serves that URL by default 
4. As a result of script execution the switch is automatically registered in Cloudvision as can be seen below

![Request Response image](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example4_cloudvision/images/inventory.png)
