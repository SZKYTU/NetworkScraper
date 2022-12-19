from pythonping import ping

# from config import IP
from dbmodule import updateStatus

import os

IP = ["10.10.80.71", 
    "10.10.80.72"]

def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            updateStatus(1, ip)
        else:
            updateStatus(0, ip)

def HNCheck():
    for ip in IP:
        askDomain = os.system(f'cmd /k "nbtstat -a {ip}"')
        print(askDomain)



# ipCheck()