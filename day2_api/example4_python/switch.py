#!/bin/python

import argparse
from jsonrpclib import Server
import logging
import logging.handlers
import re
import socket
import ssl
import sys

# Setup LOG
logging.basicConfig()
LOG = logging.getLogger(__name__)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
LOG.addHandler(handler)

LOG.setLevel(logging.DEBUG)

class Switch():
    """
    Used to run switch commands through eAPI and check command output
    """

    def __init__(self, host = None, user = None, passwd = None,
                 verify_ssl = False):

        self.host = host
        self.user = user
        self.passwd = passwd

        s = "https://{user}:{passwd}@{host}/command-api"
        self.url = s.format(user=user, passwd=passwd, host=host)
        
        self.ep = Server(self.url)

        self.verify_ssl = verify_ssl
        if not self.verify_ssl:
            ssl._create_default_https_context = ssl._create_unverified_context

    def _multilinestr_to_list(self, multilinestr = None):
        """
        Returns a list, each item been one line of a (multi)line string
        Handy for running multiple lines commands through one API call
        """

        l = [x.strip() for x in multilinestr.split('\n') if x.strip() != '']
        return l

    def run(self, cmds=None, timeout=10):
        """
        Runs commands through eAPI
        """

        socket.setdefaulttimeout(timeout)

        err = False
        r = None

        if type(cmds) is str:
            run_list = self._multilinestr_to_list(cmds)

        if type(cmds) is list:
            run_list = cmds

        LOG.debug("Calling eAPI at {} with {}".format(str(self.host), \
                                                      str(run_list)))
        try:
            r = self.ep.runCmds(1, run_list)
        except Exception as e:
            err = True
            LOG.error(str(e))

        return err, r

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="switch script")

    parser.add_argument("--loglevel", type = str, nargs = "?",
                        default="DEBUG",
                        help = "CRITICAL|ERROR|WARNING|INFO|DEBUG")

    args = parser.parse_args()

    # modify log level if required
    ll = {"CRITICAL": logging.CRITICAL,
          "ERROR": logging.ERROR,
          "WARNING": logging.WARNING,
          "INFO": logging.INFO,
          "DEBUG": logging.DEBUG}
    LOG.setLevel(ll[args.loglevel])

    LOG.info("EXITED")

    sys.exit(0)
