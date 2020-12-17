# Basic python examples
Basic examples about using python with EOS and CVP APIs

## EOS

`switchinfo.py` is an example on calling EOS API using `jsonrpclib`

```
# ./swinfo.py 10.34.0.31 10.34.0.32
10.34.0.31 version is 4.24.0F, systemid is 50:54:00:00:31:31 and NTP is synchronised
10.34.0.32 version is 4.24.0F, systemid is 50:54:00:00:32:32 and NTP is synchronised
```

`switch.py` is more like a generic class that could be used to make EOS API calls. A couple of step-by-step examples on using it follow

```
# ipython                          
Python 3.8.6 (default, Sep 30 2020, 04:00:38) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import switch

In [2]: s = switch.Switch(host="10.34.0.31", user="admin", passwd="abc123")

In [3]: s.run(["show version"])
DEBUG:switch:Calling eAPI at 10.34.0.31 with ['show version']
Out[3]: 
(False,
 [{'memTotal': 1498328,
   'uptime': 6147.42,
   'modelName': 'vEOS',
   'internalVersion': '4.24.0F-16270098.4240F',
   'mfgName': '',
   'serialNumber': '',
   'systemMacAddress': '50:54:00:00:31:31',
   'bootupTimestamp': 1608213564.0,
   'memFree': 756128,
   'version': '4.24.0F',
   'configMacAddress': '00:00:00:00:00:00',
   'isIntlVersion': False,
   'internalBuildId': 'da8d6269-c25f-4a12-930b-c3c42c12c38a',
   'hardwareRevision': '',
   'hwMacAddress': '00:00:00:00:00:00',
   'architecture': 'i686'}])
```

Apart from just `show` commands, configuration can be done too, for instance, the next example changes ethernet1 description

```
In [6]: s.run(["enable", "show interfaces ethernet 1 description"])
DEBUG:switch:Calling eAPI at 10.34.0.31 with ['enable', 'show interfaces ethernet 1 description']
Out[6]: 
(False,
 [{},
  {'interfaceDescriptions': {'Ethernet1': {'interfaceStatus': 'up',
     'description': '',
     'lineProtocolStatus': 'up'}}}])

In [7]: s.run(["enable", "configure", "interface ethernet 1", "description TESTING"])
DEBUG:switch:Calling eAPI at 10.34.0.31 with ['enable', 'configure', 'interface ethernet 1', 'description TESTING']
Out[7]: (False, [{}, {}, {}, {}])

In [8]: s.run(["enable", "show interfaces ethernet 1 description"])
DEBUG:switch:Calling eAPI at 10.34.0.31 with ['enable', 'show interfaces ethernet 1 description']
Out[8]: 
(False,
 [{},
  {'interfaceDescriptions': {'Ethernet1': {'interfaceStatus': 'up',
     'description': 'TESTING',
     'lineProtocolStatus': 'up'}}}])
```

## CVP

`cvpinfo.py` is an example on how to call CVP API, keep in mind that first we authenticate by calling to cvpservice/login/authenticate.do and that gives you back the cookie that will be used to authenticate subsequent calls (like /cvpservice/cvpInfo/getCvpInfo.do in the example)

![cvpinfo](https://github.com/aristaiberia/automation101/blob/main/day2_api/example4_python/images/CVPINFO.png)

```
# ./cvpinfo.py
CVP version is 2020.1.0
```

`cvprac_cvpinfo.py` is as well an example of calling CVP API with a very similar result as `cvpinfo.py`. However there is an important difference between the two. It is that `cvprac_cvpinfo.py` does use [cvprac](https://github.com/aristanetworks/cvprac) RESTful API client for CVP. Working with APIs is common that API wrappers offer a level of abstraction so it is easier to make the calls "abstracting" the details (ie, note that unlike `cvpinfo.py` no API URLs appear in `cvprac_cvpinfo.py`)

```
# ./cvprac_cvpinfo.py 
CVP version is 2020.1.0
```

`cvpdevices.py` is another CVP example listing the devices registered in CVP.

![cvpdevices](https://github.com/aristaiberia/automation101/blob/main/day2_api/example4_python/images/CVPDEVICES.png)

```
# ./cvpdevices.py 
vlab31 version is 4.24.0F sysid id 50:54:00:00:31:31 and ip is 10.34.0.31
vlab32 version is 4.24.0F sysid id 50:54:00:00:32:32 and ip is 10.34.0.32
```

