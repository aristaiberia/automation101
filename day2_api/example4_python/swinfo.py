#!/bin/python

from jsonrpclib import Server
import ssl
import sys

for switch in sys.argv[1:]:
    api_url = "https://admin:abc123@{}/command-api".format(switch)
    api = Server(api_url)
    ssl._create_default_https_context = ssl._create_unverified_context

    r = api.runCmds(1, ["show version", "show ntp status"])

    version = r[0].get("version")
    sysmac = r[0].get("systemMacAddress")
    ntpstatus = r[1].get("status")

    print("{} version is {}, systemid is {} and NTP is {}".
          format(switch, version, sysmac, ntpstatus))

sys.exit(0)
