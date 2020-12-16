# API explorer
Examples about embeded API explorer tool in EOS and in Cloudvision.

EOS devices and Cloudvision have an embedded tool to explore their API.

* EOS API

EOS API is disabled by default.
It can be enabled by:

```
management api http-commands
   no shutdown
```

At any point EOS API status can be seen:
```
vlab31(config)#
vlab31(config)#show management api http-commands 
Enabled:            Yes
HTTPS server:       running, set to use port 443
HTTP server:        shutdown, set to use port 80
Local HTTP server:  shutdown, no authentication, set to use port 8080
Unix Socket server: shutdown, no authentication
VRFs:               default
Hits:               9
Last hit:           159 seconds ago
Bytes in:           1116
Bytes out:          11610
Requests:           2
Commands:           2
Duration:           0.063 seconds
SSL Profile:        none
FIPS Mode:          No
QoS DSCP:           0
Log Level:          none
CSP Frame Ancestor: None
TLS Protocols:      1.0 1.1 1.2
   User        Requests       Bytes in       Bytes out    Last hit        
----------- -------------- -------------- --------------- --------------- 
   admin       2              1116           11610        159 seconds ago 

URLs                                 
------------------------------------ 
Management1 : https://10.34.0.31:443 
```

EOS API explorer can then be accesed by API pointing a browser to the API URLs. Then you can input EOS commands in the commands window, send them to the API and see all the details on how exactly the API call to run these commands works. IN the request viewer the body of the API request is shown. The response viewer shows how exactly the API response body does look like. Note also that the same API request can contain more than one command. The image shows the example for `show version` command:
![eosapiexplorer](https://github.com/aristaiberia/automation101/blob/main/day2_api/example1_apiexplorer/images/eosapiexplorer.png)

* CVP API

CVP also contains a CVP API explorer tool embeded in CVP. Unlike EOS, CVP has its API enabled by default so there is no need to explicitly enable it. It can be accesed by navigating to Settings and Tools gear icon and then `CloudVision API Documentation`

![cvpapiexplorer](https://github.com/aristaiberia/automation101/blob/main/day2_api/example1_apiexplorer/images/cvpapiexplorer.png)

Accesing to each particular functionality shows the different API methods that can be called on that functionality. The example image below shows API methods about Inventory operations.

![inventoryops](https://github.com/aristaiberia/automation101/blob/main/day2_api/example1_apiexplorer/images/inventoryops.png)

And then, accessing a particular method shows all the parameters that the method allows (including which ones are mandatory or optional), the kind of responses that the method could respond back to the caller and it also allows you to run the API call showing also, both, the API call and the response and how that API call could be writen in a curl request as can be seen in the example image below.

![method](https://github.com/aristaiberia/automation101/blob/main/day2_api/example1_apiexplorer/images/method.png)

This two tools, EOS API explorer and Cloudvision API explorer are very handy when writing scripts or programs that operate using the API.
