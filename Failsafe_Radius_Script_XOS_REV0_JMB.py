import exsh
import xmclib
from xmclib import emc_vars
from xmclib import cli
from device import api
from device.deviceutils import DeviceUtils
import re

def exosCmd(cmd):
        print cmd
        result = exsh.clicmd(cmd, True)
        print(str(result))
        return result

pattern = re.compile("(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}")
emc_cli.send("configure failsafe-account", False)
emc_cli.send("justin2023", False)
emc_cli.send("warren17", False)
emc_cli.send("warren17", False)
emc_cli.send("configure failsafe-account permit all", False)
emc_cli.send("save", False)
emc_cli.send("y", False)

#changed logic to work with exsh
device_IP_String = exosCmd('show WCSmgmt | include Primary')
print (device_IP_String)
IP_List = pattern.findall(device_IP_String)
device_IP_Final = IP_List[0]
command1 = 'configure radius mgmt-access primary server 10.60.7.103 1812 client-ip' + device_IP_Final + 'vr VR-Default'
emc_cli.send( command1 , False)
emc_cli.send('configure radius mgmt-access primary shared-secret a7z3436f2nteyf3u4n8frwpucsakk6', False)
emc_cli.send('enable radius', False)
emc_cli.send('save', False)
emc_cli.send('y', False)