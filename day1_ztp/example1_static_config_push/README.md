# ZTP Static Config Push
In this example:

1. Switches in ZTP mode make DHCP requests
2. DHCP server running the provided configuration (dhcp.conf.lab1) serves a lease with a specific Bootfilename option for each switch based on Switch's ClientID. That URL contains the switch config (vlab*.config)
3. The switch downloads the content specified in the Bootfilename URL (each switch will download its config)
4. To serve the content (switch config) in the given URLs this example uses Nginx webserver running the provided configuration (nginx.conf)
