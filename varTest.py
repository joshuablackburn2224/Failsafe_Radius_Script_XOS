import exsh

def exosCmd(cmd):
        print cmd
        result = exsh.clicmd(cmd, True)
        print(str(result))
        return result

device_IP = exosCmd('show WCSmgmt | include Primary',True)
print (device_IP)