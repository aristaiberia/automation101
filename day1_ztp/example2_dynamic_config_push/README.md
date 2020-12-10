# ZTP Dynamic Config Push
Unlike Example1 where DHCP Server serves a unique Bootfilename URL to each switch based on Switch's ClientID, this example serves the same Bootfilename URL parameter to all switches. In ZTP, when the switch requests the URL that has been received in the Bootfilename parameter the switch adds HTTP to the request that containing:

* X-Arista-SystemMAC
* X-Arista-ModelName
* X-Arista-SoftwareVersion
* X-Arista-Architecture

In this example the flow is:
1. Switches in ZTP mode make DHCP requests
2. DHCP server running the provided configuration (dhcp.conf.lab2) serves a lease with a Bootfilename option equal for all the switches and pointing to an URL that will be served by the provided Python Flask program (server.py)
3. The switch makes a HTTP request to download the URL specified in the received Bootfilename DHCP parameter. The request includes (among others) the X-Arista-SystemMAC Header that contains the switch SystemMAC which obviously is unique per switch
4. The Python Flask script is listening for requests. It has read a Jinja2 template with the switch config (config.j2). As expected the template has variables where the configuration can change from switch to switch (i.e. hostname, vlans, etc). It has also read a JSON file that contains the per-switch variables (swinfo.json) needed to render the template.
5. When a request arrives the Python Flask program gets the X-Arista-SystemMAC header and based on that knows the SystemMAC of the switch originating the request. The swinfo.json file is a dictionary with the keys been the Switches SystemMACs. The information for that switch is then loaded into a variable (sw) which, in turn, is used to render the template specifically for that switch.

This is how this is seen on the wire

![Request Response image]
(https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example2_dynamic_config_push/REQRESPDYN.png)

Running the Python Flask program can be done by:

```
export FLASK_APP=server.py
flask run --host=10.34.0.254 --port=8080                                                                  
 * Serving Flask app "server.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://10.34.0.254:8080/ (Press CTRL+C to quit)
```

For testing the Python Flask program, you could make artificial requests by using curl and passing the X-Arista-SystemMAC of your choice by running:
`curl -H "X-Arista-SystemMAC: 52:54:00:00:11:11" http://10.34.0.254:8080/dynconfig`
