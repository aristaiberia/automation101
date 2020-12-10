# ZTP Static Config Push
In this example:

1. Switches in ZTP mode make DHCP requests
2. DHCP server running the provided configuration (dhcp.conf.lab1) serves a lease with a specific Bootfilename option for each switch based on Switch's ClientID. That URL contains the switch config (vlab*.config)
3. The switch downloads the content specified in the Bootfilename URL (each switch will download its config from the given URL)
4. To serve the content (switch config) in the given URLs this example uses nginx webserver running the provided configuration (nginx.conf)

Switch will use System MAC address as ClientID in DHCP request as seen below

![systemmac](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example1_static_config_push/systemmac.png)

![discoveroffer](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example1_static_config_push/discoveroffer.png)

So each switch will request the URL served in Bootfilename DHCP parameter containing its configuration (different URL for each switch)

![reqresp](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example1_static_config_push/reqresp.png)
