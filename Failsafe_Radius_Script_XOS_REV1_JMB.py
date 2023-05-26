import xmclib
from xmclib import emc_vars
from xmclib import cli
from device import api
from device.deviceutils import DeviceUtils
# emc_vars['device_ip']

emc_cli.send("configure failsafe-account", False)
emc_cli.send("justin2023", False)
emc_cli.send("warren17", False)
emc_cli.send("warren17", False)
emc_cli.send("configure failsafe-account permit all", False)
emc_cli.send("save", False)
emc_cli.send("y", False)

#changed logic to work with exsh
device_IP = emc_vars['deviceIP']
command1 = 'configure radius mgmt-access primary server 10.60.7.103 1812 client-ip' + device_IP + 'vr VR-Default'
emc_cli.send( command1 , False)
emc_cli.send('configure radius mgmt-access primary shared-secret a7z3436f2nteyf3u4n8frwpucsakk6', False)
emc_cli.send('enable radius', False)
emc_cli.send('save', False)
emc_cli.send('y', False)